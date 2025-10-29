import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Webcam from 'react-webcam';
import { skinService } from '../services/skinService';
import { useCamera } from '../hooks/useCamera';
import ProductCard from '../components/ProductCard';
import Loader from '../components/Loader';

function DetailSkin() {
  const [analysis, setAnalysis] = useState(null);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedRegion, setSelectedRegion] = useState(null);
  const navigate = useNavigate();
  
  const { image, showCamera, webcamRef, captureImage, openCamera } = useCamera();

  const analyzeImage = async () => {
    if (!image) return;

    setLoading(true);
    try {
      const response = await skinService.analyzeSkin(image);
      setAnalysis(response.analysis);
      setProducts(response.products);
    } catch (error) {
      console.error('Analysis failed:', error);
      alert('Analysis failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleImageClick = (e) => {
    const rect = e.target.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    setSelectedRegion({ x, y });
  };

  return (
    <div className="min-h-screen bg-white pb-20">
      {/* Header */}
      <div className="bg-white border-b border-gray-200 p-4 flex items-center">
        <button onClick={() => navigate(-1)} className="mr-4 text-2xl">←</button>
        <h1 className="text-xl font-semibold">Detail Skin</h1>
      </div>

      <div className="p-6">
        {/* Initial State - No Camera, No Image */}
        {!showCamera && !image && (
          <div className="w-full h-64 bg-gray-100 rounded-2xl flex items-center justify-center">
            <button
              onClick={openCamera}
              className="px-6 py-3 bg-orange-400 text-white rounded-full font-semibold hover:bg-orange-500 transition"
            >
              Take Photo
            </button>
          </div>
        )}

        {/* Camera Active */}
        {showCamera && (
          <div className="relative">
            <Webcam
              ref={webcamRef}
              screenshotFormat="image/jpeg"
              className="w-full rounded-2xl"
              videoConstraints={{
                width: 1280,
                height: 720,
                facingMode: "user"
              }}
            />
            <button
              onClick={captureImage}
              className="absolute bottom-4 left-1/2 transform -translate-x-1/2 w-16 h-16 bg-white rounded-full shadow-lg border-4 border-orange-400 hover:scale-110 transition"
            />
          </div>
        )}

        {/* Image Captured - Before Analysis */}
        {image && !analysis && (
          <div className="relative">
            <img
              src={image}
              alt="Captured"
              className="w-full rounded-2xl cursor-pointer"
              onClick={handleImageClick}
            />
            {selectedRegion && (
              <div
                className="absolute border-2 border-red-500 w-16 h-12 pointer-events-none"
                style={{
                  left: selectedRegion.x - 32,
                  top: selectedRegion.y - 24
                }}
              />
            )}
            <button
              onClick={analyzeImage}
              disabled={loading}
              className="mt-4 w-full py-3 bg-orange-400 text-white rounded-full font-semibold disabled:bg-gray-300 hover:bg-orange-500 transition"
            >
              {loading ? <Loader /> : 'Get product recommendation'}
            </button>
          </div>
        )}

        {/* Analysis Results */}
        {analysis && (
          <div>
            <img src={image} alt="Analyzed" className="w-full rounded-2xl mb-6" />
            
            {/* Analysis Summary */}
            <div className="bg-white rounded-2xl border border-gray-200 p-6 mb-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-gray-800">
                  {analysis.pore_analysis.severity === 'minimal' ? 'Excellent' : 'Needs Care'}
                </h3>
                <span className="text-4xl font-bold text-orange-400">
                  {Math.round(analysis.overall_score)}
                </span>
              </div>

              <p className="text-gray-600 mb-6">{analysis.recommendation}</p>

              {/* Detailed Scores */}
              <div className="space-y-3">
                <div className="flex justify-between items-center">
                  <span className="text-gray-700 font-medium">Pores</span>
                  <div className="flex items-center gap-2">
                    <div className="w-32 h-2 bg-gray-200 rounded-full">
                      <div
                        className="h-full bg-orange-400 rounded-full transition-all"
                        style={{ width: `${analysis.pore_analysis.score}%` }}
                      />
                    </div>
                    <span className="text-gray-700 w-12 text-right">
                      {Math.round(analysis.pore_analysis.score)}%
                    </span>
                  </div>
                </div>

                <div className="flex justify-between items-center">
                  <span className="text-gray-700 font-medium">Acne</span>
                  <div className="flex items-center gap-2">
                    <div className="w-32 h-2 bg-gray-200 rounded-full">
                      <div
                        className="h-full bg-red-400 rounded-full transition-all"
                        style={{ width: `${analysis.acne_analysis.score}%` }}
                      />
                    </div>
                    <span className="text-gray-700 w-12 text-right">
                      {Math.round(analysis.acne_analysis.score)}%
                    </span>
                  </div>
                </div>

                <div className="flex justify-between items-center">
                  <span className="text-gray-700 font-medium">Texture</span>
                  <div className="flex items-center gap-2">
                    <div className="w-32 h-2 bg-gray-200 rounded-full">
                      <div
                        className="h-full bg-blue-400 rounded-full transition-all"
                        style={{ width: `${analysis.texture_analysis.score}%` }}
                      />
                    </div>
                    <span className="text-gray-700 w-12 text-right">
                      {Math.round(analysis.texture_analysis.score)}%
                    </span>
                  </div>
                </div>
              </div>

              <div className="mt-4 pt-4 border-t border-gray-200">
                <p className="text-sm text-gray-600">
                  <span className="font-semibold">Skin Type:</span> {analysis.skin_type}
                </p>
              </div>
            </div>

            {/* Product Recommendations */}
            {products.length > 0 && (
              <div>
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-lg font-semibold text-gray-800">Skin Care Recommendation</h3>
                  <button 
                    onClick={() => navigate('/trips')}
                    className="text-orange-500 text-sm font-semibold"
                  >
                    All
                  </button>
                </div>
                <div className="space-y-4">
                  {products.map((product) => (
                    <ProductCard key={product.id} product={product} />
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default DetailSkin;
