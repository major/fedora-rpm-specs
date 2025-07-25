 %bcond_without tests

%global pypi_name geotiler

%global _description %{expand:
GeoTiler is a library to create maps using tiles from a map provider.
The main goal of the library is to enable a programmer to create maps
using tiles downloaded from OpenStreetMap, Stamen or other map provider.
The maps can be used by interactive applications or to create data analysis
graphs.}

Name:           python-%{pypi_name}
Version:        0.15.1
Release:        7%{?dist}
Summary:        GeoTiler is a library to create map using tiles from a map provider

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/wrobell/%{pypi_name}
Source0:        %{pypi_source %{pypi_name}}

# Upstream for modestmaps-py was asked to clarify the exact BSD license
# text via https://github.com/stamen/modestmaps-py/issues/19 and by direct
# email to Michal Migurski. Since that upstream has remained unresponsive,
# the intended license text is assumed to be the 3-clause BSD license from
# https://opensource.org/licenses/BSD-3-Clause (as the more restrictive of
# the two most common BSD variants, the other being
# https://opensource.org/licenses/BSD-2-Clause).
Source1:        LICENSE-modestmaps-py
# Man pages hand-written for Fedora in groff_man(7) format based on upstream
# --help output.
Source2:        geotiler-fetch.1
Source3:        geotiler-lint.1
Source4:        geotiler-route.1

# Downstream-only: patch out linting and coverage dependencies
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          geotiler-0.15.0-linters.patch

BuildRequires:  python3-devel
BuildRequires:  make

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  pyproject-rpm-macros

#For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
#For rendered image placeholders
BuildRequires:  ImageMagick
BuildRequires:  font(liberationsans)

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
%endif

# For geotiler-route command-line tool:
Requires:       %{py3_dist pycairo}
Requires:       %{py3_dist lxml}
    
%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

rm -fv poetry.lock

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x tests}

%build
%pyproject_wheel

# Insert placeholders for documentation sample images that are normally
# generated by downloading (variously-licensed) data from the Internet in the
# top-level Makefile.
convert -size 512x512 xc:gray -font 'Liberation-Sans-Bold-Italic' \
    -pointsize 48 -fill black -gravity center -annotate +0+0 \
    'Rendered image\nnot available' doc/map-osm.png
cp -p doc/map-osm.png doc/map-stamen-toner.png
cp -p doc/map-osm.png doc/map-bluemarble.png
convert -size 1920x1080 xc:gray -font 'Liberation-Sans-Bold-Italic' \
    -pointsize 96 -fill black -gravity center -annotate +0+0 \
    'Rendered image\nnot available' doc/map-path.png
    
PYTHONPATH="${PWD}" sphinx-build -b latex doc _latex %{?_smp_mflags}
%make_build -C _latex LATEXMKOPTS='-quiet'

%install
%pyproject_install
%pyproject_save_files -l geotiler
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    geotiler-fetch.1 geotiler-lint.1 geotiler-route.1

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README
%{_bindir}/geotiler-fetch
%{_bindir}/geotiler-lint
%{_bindir}/geotiler-route
%{_mandir}/man1/geotiler-fetch.1*
%{_mandir}/man1/geotiler-lint.1*
%{_mandir}/man1/geotiler-route.1*

%files doc
%license COPYING
%doc _latex/geotiler.pdf

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 15 2025 Python Maint <python-maint@redhat.com> - 0.15.1-6
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.15.1-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Python Maint <python-maint@redhat.com> - 0.15.1-2
- Rebuilt for Python 3.13

* Fri Feb 09 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.15.1-1
- Update to 0.15.1 (close RHBZ#2259601)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.15.0-1
- Update to 0.15.0 (close RHBZ#2228274)

* Mon Jul 31 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.14.7-4
- Patch out unused uvloop test dependency
- Patch for Pillow 10 (fix RHBZ#2220253, fix RHBZ#2226199)
- Patch out unwanted linting and coverage test dependencies

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 3 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.14.7-1
- Update to the latest upstream's release
- Remove patch

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.14.5-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.14.5-2
- Do not omit first argument to pypi_source
- Reduce LaTeX PDF build verbosity
- Add extra dependencies for geotiler-route CLI tool
- Add man pages for command-line tools

* Sun Oct 17 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.14.5-1
- Initial package
