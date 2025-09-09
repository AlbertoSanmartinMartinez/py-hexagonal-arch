#!/bin/bash
# Build and publish script for py-hexagonal-arch

set -e

echo "🏗️  Building py-hexagonal-arch package..."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/

# Install/upgrade build tools
echo "📦 Installing build tools..."
python -m pip install --upgrade build twine

# Build the package
echo "🔨 Building package..."
python -m build

# Check the distribution
echo "✅ Checking distribution..."
python -m twine check dist/*

echo "📋 Package contents:"
ls -la dist/

echo ""
echo "🎉 Package built successfully!"
echo ""
echo "📤 To publish to Test PyPI:"
echo "   python -m twine upload --repository testpypi dist/*"
echo ""
echo "📤 To publish to PyPI:"
echo "   python -m twine upload dist/*"
echo ""
echo "🧪 To test install from Test PyPI:"
echo "   pip install --index-url https://test.pypi.org/simple/ py-hexagonal-arch"
echo ""
echo "💾 To install from PyPI:"
echo "   pip install py-hexagonal-arch"
