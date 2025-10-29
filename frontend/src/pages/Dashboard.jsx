import React, { useState, useEffect } from 'react';
import './Dashboard.css';

const Dashboard = () => {
  const [analysisResults, setAnalysisResults] = useState(null);
  const [productRecommendations, setProductRecommendations] = useState([]);
  
  useEffect(() => {
    // Load analysis results from localStorage or API
    const savedResults = localStorage.getItem('skinAnalysisResults');
    if (savedResults) {
      const results = JSON.parse(savedResults);
      setAnalysisResults(results);
      generateProductRecommendations(results);
    }
  }, []);

  const generateProductRecommendations = (results) => {
    // Product recommendations based on skin analysis
    const scores = results?.scores || {};
    let recommendations = [];

    if (scores.oily_score > 0.6) {
      recommendations = [
        {
          name: 'The Ordinary Niacinamide 10% + Zinc 1%',
          brand: 'The Ordinary',
          price: '£6.90',
          description: 'Oil control serum for blemish-prone skin',
          reason: 'Perfect for controlling oily skin',
          url: 'https://www.boots.com/the-ordinary-niacinamide-10-zinc-1-10267783',
          rating: 4.6
        },
        {
          name: 'Clinique Beauty Icons Star Gift',
          brand: 'Clinique', 
          price: '£44.50',
          description: 'Complete skincare routine for oily skin',
          reason: 'Comprehensive solution for oily/combination skin',
          url: 'https://www.boots.com/clinique-beauty-icons-star-gift-10369863',
          rating: 4.5
        }
      ];
    } else if (scores.dry_score > 0.6) {
      recommendations = [
        {
          name: 'CeraVe Get Your Glow On Gift Set',
          brand: 'CeraVe',
          price: '£29.50',
          description: 'Complete skincare routine for healthy glow',
          reason: 'Provides deep hydration for dry skin',
          url: 'https://www.boots.com/cerave-get-your-glow-on-gift-set-10374474',
          rating: 4.7
        },
        {
          name: 'Boots Ingredients Hyaluronic Acid Moisturiser',
          brand: 'Boots',
          price: '£3.60',
          description: 'Hydrating moisturizer for all skin types',
          reason: 'Affordable daily hydration solution',
          url: 'https://www.boots.com/boots-ingredients-hyaluronic-acid-moisturiser-30ml-10276161',
          rating: 4.2
        }
      ];
    } else if (scores.wrinkle_score > 0.5) {
      recommendations = [
        {
          name: 'DIOR Capture Anti-Aging Gift Set',
          brand: 'DIOR',
          price: '£109.00',
          description: 'Limited edition anti-aging skincare collection',
          reason: 'Premium anti-aging formula for mature skin',
          url: 'https://www.boots.com/dior-capture-anti-aging-gift-set-limited-edition--10368981',
          rating: 4.8
        },
        {
          name: 'No7 The Ultimate Skincare Collection Gift Set',
          brand: 'No7',
          price: '£39.00',
          description: 'Complete anti-aging skincare routine',
          reason: 'Proven anti-aging ingredients at great value',
          url: 'https://www.boots.com/no7-the-ultimate-skincare-collection-gift-set-10364646',
          rating: 4.5
        }
      ];
    } else {
      recommendations = [
        {
          name: 'The Ordinary Glycolic Acid 7% Exfoliating Toner',
          brand: 'The Ordinary',
          price: '£8.90',
          description: 'Exfoliating toner for improved skin texture',
          reason: 'Great for maintaining healthy skin',
          url: 'https://www.boots.com/the-ordinary-glycolic-acid-7-exfoliating-solution-100ml-10335078',
          rating: 4.4
        },
        {
          name: 'Super Facialist Vitamin C+ Brighten Gentle Daily Micro Polish Wash',
          brand: 'Super Facialist',
          price: '£6.67',
          description: 'Gentle daily cleanser with vitamin C',
          reason: 'Perfect for daily skincare routine',
          url: 'https://www.boots.com/superfacialist-vitamin-c-gentle-daily-micro-polish-wash-125ml-10160292',
          rating: 4.3
        }
      ];
    }

    setProductRecommendations(recommendations.slice(0, 2));
  };

  // ...existing code for rendering analysis results...

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>Your Skin Analysis Dashboard</h1>
        <p>Personalized insights and product recommendations</p>
      </div>

      {analysisResults ? (
        <div className="dashboard-content">
          {/* Existing analysis results sections */}
          
          {/* Product Recommendations Section */}
          <div className="recommendations-section">
            <h2>🛍️ Recommended Products for You</h2>
            <p>Based on your skin analysis, here are the top 2 products we recommend:</p>
            
            <div className="product-recommendations">
              {productRecommendations.map((product, index) => (
                <div key={index} className="product-card">
                  <div className="product-header">
                    <h3>{product.name}</h3>
                    <span className="product-brand">{product.brand}</span>
                  </div>
                  
                  <div className="product-details">
                    <p className="product-description">{product.description}</p>
                    <div className="product-info">
                      <span className="product-price">{product.price}</span>
                      <span className="product-rating">⭐ {product.rating}</span>
                    </div>
                  </div>
                  
                  <div className="product-reason">
                    <strong>Why we recommend this:</strong>
                    <p>{product.reason}</p>
                  </div>
                  
                  <a 
                    href={product.url} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="product-link"
                  >
                    View on Boots →
                  </a>
                </div>
              ))}
            </div>
          </div>
        </div>
      ) : (
        <div className="no-results">
          <p>No analysis results found. Please complete a skin analysis first.</p>
          <a href="/analyze" className="cta-button">Start Analysis</a>
        </div>
      )}
    </div>
  );
};

export default Dashboard;