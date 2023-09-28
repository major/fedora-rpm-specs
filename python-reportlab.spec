%global cmapdir %(echo `rpm -qls ghostscript | grep CMap | awk '{print $2}'`)
%global pypi_name reportlab

%global debug_package %{nil}

%bcond_without tests

Name:           python-%{pypi_name}
Version:        4.0.5
Release:        %autorelease
Summary:        Library for generating PDFs and graphics
License:        BSD and GPLv2+
URL:            https://www.reportlab.com/opensource/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  freetype-devel
BuildRequires:  ghostscript
Buildrequires:  fontpackages-devel
%global fonts font(dejavusans)
BuildRequires:  %{fonts}

Obsoletes:      %{name}-doc < 0:3.5.21-1

%description
This is the ReportLab PDF Toolkit. It allows rapid creation of rich PDF
documents, and also creation of charts in a variety of bitmap and vector
formats.

%package -n     python3-%{pypi_name}
Summary:        Library for generating PDFs and graphics
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pillow
Requires:       %{fonts}
%py_provides python3-%{pypi_name}
Obsoletes: python2-reportlab < 0:%{version}-%{release}

%description -n python3-%{pypi_name}
This is the ReportLab PDF Toolkit. It allows rapid creation of rich PDF 
documents, and also creation of charts in a variety of bitmap and vector 
formats.

%prep
%autosetup -n %{pypi_name}-%{version}

# clean up hashbangs from libraries
find src -name '*.py' | xargs sed -i -e '/^#!\//d'
# patch the CMap path by adding Fedora ghostscript path before the match
sed -i '/\~\/\.local\/share\/fonts\/CMap/i''\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ '\'%{cmapdir}\''\,' src/reportlab/rl_settings.py

# Remove Upstream Egg
rm -rf src/reportlab.egg-info

# Remove bundled libart
rm -rf src/rl_addons/renderPM/libart_lgpl

%build
CFLAGS="%{build_cflags} -Isrc/rl_addons/renderPM" \
 %py3_build -- --no-download-t1-files

%install
CFLAGS="%{build_cflags} -Isrc/rl_addons/renderPM" \
 %py3_install -- --no-download-t1-files

# Unbundled fonts
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Regular") %{buildroot}%{python3_sitelib}/reportlab/fonts/Vera.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Bold Oblique") %{buildroot}%{python3_sitelib}/reportlab/fonts/VeraBI.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Bold") %{buildroot}%{python3_sitelib}/reportlab/fonts/VeraBd.ttf
ln -sf $(fc-match -f "%{file}" "DejaVu Sans:style=Condensed Oblique") %{buildroot}%{python3_sitelib}/reportlab/fonts/VeraIt.ttf

rm -f %{buildroot}%{python3_sitelib}/reportlab/fonts/bitstream-vera-license.txt

cp -a demos %{buildroot}%{python3_sitelib}/reportlab/
cp -a tools %{buildroot}%{python3_sitelib}/reportlab/

# Fix shebang in individual files
%py3_shebang_fix %{buildroot}%{python3_sitelib}/reportlab/demos/tests/testdemos.py
%py3_shebang_fix %{buildroot}%{python3_sitelib}/reportlab/tools/docco/docpy.py
%py3_shebang_fix %{buildroot}%{python3_sitelib}/reportlab/tools/docco/graphdocpy.py
%py3_shebang_fix %{buildroot}%{python3_sitelib}/reportlab/tools/docco/rl_doc_utils.py
%py3_shebang_fix %{buildroot}%{python3_sitelib}/reportlab/tools/pythonpoint/pythonpoint.py

chmod 0755 %{buildroot}%{python3_sitelib}/reportlab/demos/tests/testdemos.py
chmod 0755 %{buildroot}%{python3_sitelib}/reportlab/tools/docco/docpy.py
chmod 0755 %{buildroot}%{python3_sitelib}/reportlab/tools/docco/graphdocpy.py
chmod 0755 %{buildroot}%{python3_sitelib}/reportlab/tools/docco/rl_doc_utils.py
chmod 0755 %{buildroot}%{python3_sitelib}/reportlab/tools/pythonpoint/pythonpoint.py

%if %{with tests}
%check
# Tests need in-build compiled Python modules to be executed
# Tests pre-generate userguide PDF
cp -a build/lib/reportlab tests/
cp -a build/lib/reportlab docs/
cp -a build/lib/reportlab docs/userguide/
%{__python3} setup.py tests
%endif

%files -n python3-%{pypi_name}
%doc README.txt CHANGES.md docs/reportlab-userguide.pdf
%license LICENSE
%{python3_sitelib}/reportlab/
%{python3_sitelib}/reportlab-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
