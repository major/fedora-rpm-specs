%global pypi_name commoncode

Name:           python-%{pypi_name}
Version:        32.3.0
Release:        %autorelease
Summary:        Common functions and utilities for handling paths, dates, files and hashes

# Python-2.0:
#  - src/commoncode/dict_utils.py
#  - src/commoncode/fileutils.py
# LicenseRef-Fedora-Public-Domain: src/commoncode/functional.py
License:        Apache-2.0 AND Python-2.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/nexB/commoncode
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
# The docs extra was removed, so specify this manually
# based on the dependencies in the dev extra.
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinx-reredirects}
BuildRequires:  %{py3_dist sphinx-copybutton}

%global common_description %{expand:
Commoncode provides a set of common functions and utilities for handling various
things like paths, dates, files and hashes. It started as library in
scancode-toolkit.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml
sed -i \
    -e 's|requests\[use_chardet_on_py3\]|requests|' \
    -e 's|Beautifulsoup4\[chardet\]|Beautifulsoup4|' \
    -e '/doc8/d' \
    -e '/sphinx-rtd-dark-mode/d' \
    -e '/sphinx-autobuild/d' \
    -e 's/click >=.*/click/' \
setup.cfg
sed -i '/"sphinx_rtd_dark_mode"/d' docs/source/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
export LC_ALL=C.UTF-8
%if 0%{?fedora} < 40
%pytest
%else
# https://github.com/aboutcode-org/commoncode/issues/56
# https://github.com/aboutcode-org/commoncode/issues/88
%pytest -k "not test_safe_path_posix_style_chinese_char and not test_get_type"
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CODE_OF_CONDUCT.rst README.rst
%license etc/scripts/gen_pypi_simple.py.NOTICE
%license src/commoncode/dict_utils.ABOUT
%license src/commoncode/python.LICENSE

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
