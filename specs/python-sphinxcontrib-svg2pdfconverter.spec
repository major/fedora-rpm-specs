%global forgeurl https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter

Version:        1.3.0

%forgemeta

%global srcname sphinxcontrib-svg2pdfconverter

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Sphinx SVG to PDF Converter Extension

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%generate_buildrequires
%pyproject_buildrequires


%description
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).


%package -n python3-%{srcname}-common
Summary:        Sphinx SVG to PDF Converter Extension - common files

%description -n python3-%{srcname}-common
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains common files.


%package -n python3-sphinxcontrib-inkscapeconverter
Summary:        Sphinx SVG to PDF Converter Extension - Inkscape converter

Requires:       /usr/bin/inkscape
Requires:       python3-%{srcname}-common = %{version}-%{release}

%description -n python3-sphinxcontrib-inkscapeconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using Inkscape.


%package -n python3-sphinxcontrib-rsvgconverter
Summary:        Sphinx SVG to PDF Converter Extension - libRSVG converter

Requires:       /usr/bin/rsvg-convert
Requires:       python3-%{srcname}-common = %{version}-%{release}

%description -n python3-sphinxcontrib-rsvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using libRSVG.


%package -n python3-sphinxcontrib-cairosvgconverter
Summary:        Sphinx SVG to PDF Converter Extension - CairoSVG converter

Requires:       %{py3_dist CairoSVG}
Requires:       python3-%{srcname}-common = %{version}-%{release}

%description -n python3-sphinxcontrib-cairosvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using CairoSVG.


%prep
%forgeautosetup


%build
%pyproject_wheel


%install
%pyproject_install


#check
#{__python3} setup.py test


# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}-common
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/sphinxcontrib/__init__.py
%{python3_sitelib}/sphinxcontrib/__pycache__/__init__.*.pyc
%{python3_sitelib}/sphinxcontrib_svg2pdfconverter-%{version}.dist-info/


%files -n python3-sphinxcontrib-inkscapeconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/inkscapeconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/inkscapeconverter.py


%files -n python3-sphinxcontrib-rsvgconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/rsvgconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/rsvgconverter.py


%files -n python3-sphinxcontrib-cairosvgconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/cairosvgconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/cairosvgconverter.py


%changelog
%autochangelog
