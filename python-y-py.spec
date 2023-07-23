Name:           python-y-py
Version:        0.6.0
Release:        4%{?dist}
Summary:        Python bindings for the Y-CRDT built from yrs (Rust)
License:        MIT
URL:            https://github.com/y-crdt/ypy
Source:         %{pypi_source y_py}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  rust-packaging

%global _description %{expand:
Ypy is a Python binding for Y-CRDT. 
It provides distributed data types that
enable real-time collaboration between devices.}


%description %_description

%package -n     python3-y-py
Summary:        %{summary}
# Statically linked deps and their licenses.
# When updating, check the generated LICENSE.dependencies file.
#
# python-y-py code is MIT
# Apache-2.0: pyo3 v0.16.6
# Apache-2.0: pyo3-ffi v0.16.6
# MIT OR Apache-2.0: cfg-if v0.1.10
# MIT OR Apache-2.0: cfg-if v1.0.0
# MIT OR Apache-2.0: getrandom v0.1.15
# MIT OR Apache-2.0: libc v0.2.139
# MIT OR Apache-2.0: lock_api v0.4.9
# MIT OR Apache-2.0: parking_lot v0.12.1
# MIT OR Apache-2.0: parking_lot_core v0.9.5
# MIT OR Apache-2.0: ppv-lite86 v0.2.17
# MIT OR Apache-2.0: rand v0.7.3
# MIT OR Apache-2.0: rand_chacha v0.2.2
# MIT OR Apache-2.0: rand_core v0.5.1
# MIT OR Apache-2.0: scopeguard v1.1.0
# MIT OR Apache-2.0: smallstr v0.2.0
# MIT OR Apache-2.0: smallvec v1.10.0
# MIT OR Apache-2.0: thiserror v1.0.37
# MIT OR Apache-2.0: unindent v0.1.11
# MIT: lib0 v0.12.2
# MIT: yrs v0.12.2
License: MIT AND (MIT OR Apache-2.0) AND Apache-2.0

%description -n python3-y-py %_description


%prep
%autosetup -p1 -n y_py-%{version}
# Fedora has maturin 1.0.0 which is pretty much compatible with 0.14;
# we relax the upper bound entirely -- if it builds, it's probably OK.
sed -i 's/maturin>=0.14,<0.15/maturin>=0.14/' pyproject.toml
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires
%pyproject_buildrequires


%build
export RUSTFLAGS="%build_rustflags"
%pyproject_wheel
%{cargo_license} > LICENSE.dependencies


%install
%pyproject_install
%pyproject_save_files y_py


%check
%pytest


%files -n python3-y-py -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE.dependencies


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.12

* Mon May 22 2023 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Use maturin to build this package, as it is finally available in Fedora

* Thu Feb 23 2023 Lumír Balhar <lbalhar@redhat.com> - 0.6.0-1
- Update to 0.6.0 (rhbz#2171402)

* Thu Dec 15 2022 Lumír Balhar <lbalhar@redhat.com> - 0.5.5-1
- Initial package