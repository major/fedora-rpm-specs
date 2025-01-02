%global modname bcrypt
%global sum     Modern password hashing for your software and your servers

Name:               python-bcrypt
Version:            4.2.1
Release:            %autorelease
Summary:            %{sum}

#crypt_blowfish code is in Public domain and all other code in ASL 2.0
License:            Apache-2.0 AND LicenseRef-Fedora-Public-Domain
URL:                http://pypi.python.org/pypi/bcrypt
Source0:            %pypi_source bcrypt

%description
%{sum}.


%package -n python3-%{modname}
Summary:            %{sum}
# LICENSE.dependencies contains a full license breakdown
License:            Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND BSD-3-Clause AND MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
BuildRequires:      python3-devel
BuildRequires:      rust-packaging

%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{version} -p1
%cargo_prep
rm src/_bcrypt/Cargo.lock

%generate_buildrequires
%pyproject_buildrequires -t
(cd src/_bcrypt
%cargo_generate_buildrequires
)


%build
export RUSTFLAGS="%build_rustflags --cfg pyo3_unsafe_allow_subinterpreters"
%pyproject_wheel

(cd src/_bcrypt
%cargo_license_summary
%{cargo_license} > ../../LICENSE.dependencies
)


%install
%pyproject_install
%pyproject_save_files bcrypt


%check
%tox


%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.rst
%license LICENSE LICENSE.dependencies


%changelog
%autochangelog
