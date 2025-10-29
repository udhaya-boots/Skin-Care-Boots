import React from 'react';

function TipCard({ tip, bgColor = 'bg-green-100' }) {
  const getBgColorClass = (type) => {
    switch(type) {
      case 'good':
        return 'bg-green-100';
      case 'warning':
        return 'bg-orange-200';
      case 'info':
        return 'bg-blue-100';
      default:
        return bgColor;
    }
  };

  return (
    <div
      className={`min-w-[200px] p-6 rounded-2xl ${getBgColorClass(tip.tip_type || 'good')} transition-transform hover:scale-105 cursor-pointer`}
    >
      <h4 className="font-semibold text-gray-800 mb-2 line-clamp-2">{tip.title}</h4>
      <p className="text-sm text-gray-600 line-clamp-3">{tip.description}</p>
      
      <div className="mt-4 flex justify-end">
        <div className="w-8 h-8 bg-white bg-opacity-50 rounded-full flex items-center justify-center hover:bg-opacity-70 transition">
          <span className="text-gray-700 text-lg">?</span>
        </div>
      </div>
    </div>
  );
}

export default TipCard;
