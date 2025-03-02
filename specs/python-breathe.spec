%global owner michaeljones
%global srcname breathe
%global _description \
Breathe is an extension to reStructuredText and Sphinx to be able to read and \
render the Doxygen xml output.

# This is buildroot only in RHEL, and building the docs pulls in unwanted dependencies
%bcond doc %{undefined rhel}

Name:           python-%{srcname}
Version:        4.36.0
Release:        %autorelease
Summary:        Adds support for Doxygen xml output to reStructuredText and Sphinx

License:        BSD-3-Clause
URL:            https://github.com/%{owner}/%{srcname}
Source0:        %{URL}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  doxygen >= 1.8.4
BuildRequires:  python%{python3_pkgversion}-devel

# NOTE: git is only needed because part of the build process checks if it's in
# a git repo
BuildRequires:  git
BuildRequires:  make

# Set the name of the documentation directory
%global _docdir_fmt %{name}

%description %_description

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:       doxygen >= 1.8.4
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%package        doc
Summary:        Documentation files for %{srcname}
# tinyxml uses zlib license
License:        BSD-3-Clause AND Zlib

%description    doc
This package contains documentation for developer documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test%{?with_doc:,docs}

%build
%pyproject_wheel
%if %{with doc}
# Build the documentation
# Remove -W (turn warnings into errors) from SPHINXOPTS to fix the build for f39
%make_build SPHINXOPTS="-v -E" DOXYGEN=$(which doxygen) PYTHONPATH=$(pwd) html
# Remove temporary build files
rm documentation/build/html/.buildinfo
%endif

%install
%pyproject_install

%pyproject_save_files breathe

%check
%pytest -v tests

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/breathe-apidoc
%license LICENSE

%if %{with doc}
%files doc
%doc documentation/build/html
%license LICENSE
%endif

%changelog
%autochangelog
