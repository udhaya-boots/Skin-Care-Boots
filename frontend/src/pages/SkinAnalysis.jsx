import React, { useState } from 'react';

const SkinAnalysisResults = ({ mockResults }) => {
  // Add product recommendations to analysis results
  const [productRecommendations, setProductRecommendations] = useState([]);

  const generateProductRecommendations = (scores) => {
    let recommendations = [];

    if (scores.oily_score > 0.6 || scores.acne_score > 0.5) {
      recommendations = [
        {
          name: 'The Ordinary Niacinamide 10% + Zinc 1%',
          brand: 'The Ordinary',
          price: '£6.90',
          reason: 'Perfect for controlling oily skin and reducing blemishes',
          url: 'https://www.boots.com/the-ordinary-niacinamide-10-zinc-1-10267783',
          rating: 4.6
        },
        {
          name: 'Clinique Beauty Icons Star Gift',
          brand: 'Clinique', 
          price: '£44.50',
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
          reason: 'Provides deep hydration for dry skin',
          url: 'https://www.boots.com/cerave-get-your-glow-on-gift-set-10374474',
          rating: 4.7
        },
        {
          name: 'Boots Ingredients Hyaluronic Acid Moisturiser',
          brand: 'Boots',
          price: '£3.60',
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
          reason: 'Premium anti-aging formula for mature skin',
          url: 'https://www.boots.com/dior-capture-anti-aging-gift-set-limited-edition--10368981',
          rating: 4.8
        },
        {
          name: 'No7 The Ultimate Skincare Collection Gift Set',
          brand: 'No7',
          price: '£39.00',
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
          reason: 'Great for maintaining healthy skin texture',
          url: 'https://www.boots.com/the-ordinary-glycolic-acid-7-exfoliating-solution-100ml-10335078',
          rating: 4.4
          brand: 'Super Facialist',
          price: '£6.67',
          reason: 'Perfect for daily skincare routine',
          url: 'https://www.boots.com/superfacialist-vitamin-c-gentle-daily-micro-polish-wash-125ml-10160292',
          rating: 4.3
        }
      ];
    }

    setProductRecommendations(recommendations.slice(0, 2));
  };

  // Update the analysis function to include product recommendations
  const analyzeImage = async (file) => {
    // ...existing analysis code...
    
    // After getting the analysis results, generate product recommendations
    if (mockResults && mockResults.scores) {
      generateProductRecommendations(mockResults.scores);
      
      // Save results with recommendations to localStorage
      const resultsWithRecommendations = {
        ...mockResults,
        productRecommendations: productRecommendations
      };
      localStorage.setItem('skinAnalysisResults', JSON.stringify(resultsWithRecommendations));
    }
  };