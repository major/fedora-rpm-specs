%global modname bcrypt
%global sum     Modern password hashing for your software and your servers

Name:               python-bcrypt
Version:            4.3.0
Release:            %autorelease
Summary:            %{sum}

#crypt_blowfish code is in Public domain and all other code in ASL 2.0
License:            Apache-2.0 AND LicenseRef-Fedora-Public-Domain
URL:                https://pypi.python.org/pypi/bcrypt
Source0:            %pypi_source bcrypt

# Update pyo3 dependency from 0.23 to 0.29
# Addresses RUSTSEC-2026-0176 and RUSTSEC-2026-0177.
#
# Bump pyo3 from 0.23.5 to 0.24.0 in /src/_bcrypt
# https://github.com/pyca/bcrypt/pull/998
# Bump pyo3 from 0.24.0 to 0.24.1 in /src/_bcrypt
# https://github.com/pyca/bcrypt/pull/1016
# Bump pyo3 from 0.24.1 to 0.24.2 in /src/_bcrypt
# https://github.com/pyca/bcrypt/pull/1019
# Bump pyo3 from 0.24.2 to 0.25.0 in /src/_bcrypt
# https://github.com/pyca/bcrypt/pull/1025
# Bump pyo3 from 0.25.0 to 0.25.1 in /src/_bcrypt
# https://github.com/pyca/bcrypt/pull/1035
# Bump pyo3 version [to 0.26]
# https://github.com/pyca/bcrypt/pull/1062
# Bump pyo3 from 0.26.0 to 0.27.0 in /src/_bcrypt
# https://github.com/pyca/bcrypt/pull/1095
# Bump pyo3 from 0.27.2 to 0.28.0 in /src/_bcrypt
# https://github.com/pyca/bcrypt/pull/1148
# Bump pyo3 from 0.28.3 to 0.29.0 in /src/_bcrypt
# https://github.com/pyca/bcrypt/pull/1215
Patch:          python-bcrypt-4.3.0-pyo3.patch

%description
%{sum}.


%package -n python3-%{modname}
Summary:            %{sum}
# Includes statically linked Rust dependencies from %%{cargo_license_summary}:
#
# Apache-2.0 OR MIT
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:            %{shrink:
    Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND
    BSD-3-Clause AND
    MIT AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
# LICENSE.dependencies contains a full license breakdown
BuildRequires:      cargo-rpm-macros

%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{version} -p1
%cargo_prep
rm src/_bcrypt/Cargo.lock

%generate_buildrequires
%pyproject_buildrequires -x tests
(cd src/_bcrypt
%cargo_generate_buildrequires
)


%build
export RUSTFLAGS="%build_rustflags --cfg pyo3_unsafe_allow_subinterpreters"
(cd src/_bcrypt
%cargo_license_summary
%{cargo_license} > ../../LICENSE.dependencies
)
%pyproject_wheel



%install
%pyproject_install
%pyproject_save_files -l bcrypt


%check
%pytest


%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
