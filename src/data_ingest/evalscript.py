evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B4", "B3", "B2"],  // Bands for True Color (Red, Green, Blue)
    output: [{ id: "true_color", bands: 3, sampleType: "UINT8" }]
  };
}

function evaluatePixel(sample) {
  return [sample.B4, sample.B3, sample.B2];  // RGB color for True Color
}
"""
