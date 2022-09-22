%global srcname service-identity
%global libname service_identity

%global common_description %{expand:
Use this package if you use pyOpenSSL and don’t want to be MITMed, or if you
want to verify that a PyCA cryptography certificate is valid for a certain
hostname or IP address.  service-identity aspires to give you all the tools you
need for verifying whether a certificate is valid for the intended purposes.
In the simplest case, this means host name verification.  However,
service-identity implements RFC 6125 fully and plans to add other relevant RFCs
too.}

Name:           python-%{srcname}
Version:        21.1.0
Release:        %autorelease
Summary:        Service identity verification for pyOpenSSL

License:        MIT
URL:            https://github.com/pyca/service-identity
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Revert theme change as "furo" theme is not packaged
Patch0:         0001-Revert-theme-change.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%pyproject_extras_subpkg -n python3-%{srcname} idna

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x idna

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{libname}

%check
%pytest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files -n python-%{srcname}-doc
%doc html
%license LICENSE docs/license.rst

%changelog
%autochangelog
