%bcond_without optional_tests

Name:           python-sphinxcontrib-websupport
Version:        1.2.7
Release:        %autorelease
Summary:        Sphinx API for Web Apps

License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-websupport
Source:         %{pypi_source sphinxcontrib_websupport}
# Compatibility with Sphinx 9+
Patch:          https://github.com/sphinx-doc/sphinxcontrib-websupport/pull/91.patch
BuildArch:      noarch

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%package -n     python3-sphinxcontrib-websupport
Summary:        %{summary}
BuildRequires:  python3-devel

%if %{with optional_tests}
# Optional tests dep, undeclared upstream, can be skipped if needed
BuildRequires:  python3-xapian
%endif

%description -n python3-sphinxcontrib-websupport
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%pyproject_extras_subpkg -n python3-sphinxcontrib-websupport whoosh

%prep
%autosetup -n sphinxcontrib_websupport-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxcontrib

%check
%tox

%files -n python3-sphinxcontrib-websupport -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
