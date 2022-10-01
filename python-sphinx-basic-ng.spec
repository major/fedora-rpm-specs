%global prerel beta1

# The documentation and tests need furo.  But to build furo at all, we need
# this package.
%bcond_with bootstrap

Name:           python-sphinx-basic-ng
Version:        1.0.0
Release:        0.1.%{prerel}%{?dist}
Summary:        Modernized skeleton for Sphinx themes

License:        MIT
URL:            https://sphinx-basic-ng.readthedocs.io/
Source0:        https://github.com/pradyunsg/sphinx-basic-ng/archive/%{version}.%{prerel}/sphinx-basic-ng-%{version}.%{prerel}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wheel}

%if %{without bootstrap}
BuildRequires:  python-sphinx-doc
BuildRequires:  python3-docs
BuildRequires:  %{py3_dist furo}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist myst-parser}
BuildRequires:  %{py3_dist sphinx-copybutton}
BuildRequires:  %{py3_dist sphinx-inline-tabs}
%endif

%global _description A modernized skeleton for Sphinx themes.

%description
%_description

%package     -n python3-sphinx-basic-ng
Summary:        Modernized skeleton for Sphinx themes

%description -n python3-sphinx-basic-ng
%_description

%if %{without bootstrap}
%package        doc
Summary:        Documentation for %{name}
# This project is MIT.  Other files bundled with the documentation have the
# following licenses:
# - searchindex.js: MIT
# - _static/basic.css: BSD-2-Clause
# - _static/clipboard.min.js: MIT
# - _static/copy*: MIT
# - _static/doctools.js: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/pygments.css: BSD-2-Clause
# - _static/scripts/*: MIT
# - _static/searchtools.js: BSD-2-Clause
# - _static/styles/*: MIT
# - _static/underscore*.js: MIT
License:        MIT AND BSD-2-Clause

%description    doc
Documentation for %{name}.
%endif

%prep
%autosetup -n sphinx-basic-ng-%{version}.%{prerel}

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

%build
%pyproject_wheel

%if %{without bootstrap}
# Build documentation
PYTHONPATH=$PWD/src sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}
%endif

%install
%pyproject_install
%pyproject_save_files sphinx_basic_ng

%check
# The nox tests require network access, so we do not run them
%pyproject_check_import

%files -n python3-sphinx-basic-ng -f %{pyproject_files}
%doc README.md

%if %{without bootstrap}
%files doc
%doc html
%license LICENSE
%endif

%changelog
* Fri Sep 30 2022 Jerry James <loganjerry@gmail.com> - 1.0.0-0.1.beta1%{?dist}
- Version 1.0.0.beta1
- Drop upstreamed -sphinx patch

* Thu Aug 25 2022 Jerry James <loganjerry@gmail.com> - 0.0.1-0.1.a12
- Initial RPM
