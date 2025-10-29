import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { productService } from '../services/productService';
import { skinService } from '../services/skinService';
import { useAuth } from '../context/AuthContext';
import BottomNav from '../components/BottomNav';
import ProductCard from '../components/ProductCard';
import TipCard from '../components/TipCard';
import Loader from '../components/Loader';

function Home() {
  const [products, setProducts] = useState([]);
  const [tips, setTips] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  const { user } = useAuth();

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [productsRes, tipsRes] = await Promise.all([
        productService.getTopProducts(),
        skinService.getTips()
      ]);
      setProducts(productsRes.products);
      setTips(tipsRes.tips);
    } catch (error) {
      console.error('Failed to fetch data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-white pb-20">
      {/* Header */}
      <div className="bg-white p-6">
        <h2 className="text-2xl font-bold text-gray-800">
          Good afternoon,<br />{user?.name || 'User'}
        </h2>
      </div>

      {/* Tips Section */}
      <div className="px-6 mb-8">
        <h3 className="text-lg font-semibold text-gray-700 mb-4">Tips</h3>
        <div className="flex gap-4 overflow-x-auto hide-scrollbar">
          {tips.map((tip, index) => (
            <TipCard 
              key={tip.id} 
              tip={tip} 
              bgColor={index % 2 === 0 ? 'bg-green-100' : 'bg-orange-200'} 
            />
          ))}
        </div>
      </div>

      {/* Products Section */}
      <div className="px-6">
        <h3 className="text-lg font-semibold text-gray-700 mb-4">
          Skin care product
        </h3>
        {loading ? (
          <div className="text-center py-8">
            <Loader />
          </div>
        ) : (
          <div className="space-y-4">
            {products.map((product) => (
              <ProductCard
                key={product.id}
                product={product}
                onClick={() => navigate('/detail', { state: { product } })}
              />
            ))}
          </div>
        )}
      </div>

      <BottomNav />
    </div>
  );
}

export default Home;
