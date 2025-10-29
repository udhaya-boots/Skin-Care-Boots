import React from 'react';

function ProductCard({ product, onClick }) {
  return (
    <div
      onClick={() => onClick && onClick(product)}
      className="bg-white border border-gray-200 rounded-2xl p-4 flex items-center gap-4 cursor-pointer hover:shadow-lg transition-shadow duration-200"
    >
      <div className="w-20 h-20 bg-gray-100 rounded-xl flex items-center justify-center flex-shrink-0">
        <span className="text-3xl">🧴</span>
      </div>
      
      <div className="flex-1 min-w-0">
        <h4 className="font-semibold text-gray-800 truncate">{product.name}</h4>
        <p className="text-sm text-gray-600 mt-1 line-clamp-2">{product.description}</p>
        
        <div className="flex items-center justify-between mt-2">
          {product.is_top_product ? (
            <span className="text-xs text-orange-500 font-medium">🔥 Top produk</span>
          ) : (
            <span className="text-xs text-green-600 font-medium">✓ Direkomendasikan untuk anda</span>
          )}
          
          {product.rating && (
            <div className="flex items-center text-xs text-gray-600">
              <span className="text-yellow-400 mr-1">⭐</span>
              {product.rating.toFixed(1)}
            </div>
          )}
        </div>
        
        {product.price && (
          <p className="text-sm font-semibold text-gray-800 mt-1">
            Rp {product.price.toLocaleString('id-ID')}
          </p>
        )}
      </div>
    </div>
  );
}

export default ProductCard;
