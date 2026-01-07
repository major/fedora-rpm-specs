%{!?postgresql_default:%global postgresql_default 0}

%global shortname       anonymizer
%global extension       postgresql_%{shortname}
%global pgversion       16
%global pgrx_version    0.16.1
%global pg_config       %{_bindir}/pg_config

Name:           postgresql%{pgversion}-%{shortname}
Version:        2.5.1
Release:        %autorelease
Summary:        Mask or replace personally identifiable information (PII) or sensitive data

# postgresql_anonymizer: PostgreSQL
# Rust dependencies:
# NCSA
# Unicode-3.0
# (0BSD OR MIT OR Apache-2.0)
# (Apache-2.0 OR BSL-1.0)
# (Apache-2.0 OR MIT)
# (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
# Apache-2.0 WITH LLVM-exception
# Apache-2.0
# (BSD-2-Clause OR Apache-2.0 OR MIT)
# BSD-2-Clause
# BSD-3-Clause
# (MIT OR Apache-2.0 OR LGPL-2.1-or-later)
# (MIT OR Apache-2.0 OR Zlib)
# MIT
# (Unlicense OR MIT)
# Zlib

License:        %{shrink:
    PostgreSQL AND
    NCSA AND
    Unicode-3.0 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    Apache-2.0 WITH LLVM-exception AND
    Apache-2.0 AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    MIT AND
    (Unlicense OR MIT) AND
    Zlib
}

URL:            https://gitlab.com/dalibo/%{extension}
Source0:        https://gitlab.com/dalibo/%{extension}/-/archive/%{version}/%{extension}-%{version}.tar.bz2
# Generated with script below (like https://src.fedoraproject.org/rpms/task/blob/rawhide/f/task.spec)
Source1:        %{extension}-%{version}-vendored.tar.xz
# To create a tarball with all crates vendored (like https://src.fedoraproject.org/rpms/loupe/blob/rawhide/f/loupe.spec)
Source2:        create-vendored-tarball.sh
# Change default feature to the correct pg version and remove tests from dependencies, the lack of tests is justified below
Patch:          anonymizer-cargo.patch
Patch:          remove-disallowed-licenses.patch

# drop i686 support (https://fedoraproject.org/wiki/Changes/Noi686Repositories)
ExcludeArch:    %{ix86}

%if %?postgresql_default
%global pkgname %{extension}
%package -n %{pkgname}
Summary:        Mask or replace personally identifiable information (PII) or sensitive data
%else
%global pkgname %name
%endif

BuildRequires:  rustfmt
BuildRequires:  clang
BuildRequires:  bison-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  wget
BuildRequires:  postgresql%{pgversion}-server
BuildRequires:  postgresql%{pgversion}-server-devel
BuildRequires:  cargo-rpm-macros >= 26
Requires:       postgresql%{pgversion}-server

%global precise_version %{?epoch:%epoch:}%version-%release
Provides: %{pkgname} = %precise_version
%if %?postgresql_default
Provides: %name = %precise_version
Provides: postgresql-%{extension} = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{extension}-any
Conflicts: %{extension}-any

%description
PostgreSQL Anonymizer is an extension to mask or replace
personally identifiable information (PII) or commercially sensitive data from
a PostgreSQL database.
The project has a declarative approach of anonymization. This means you can
declare the masking rules using the PostgreSQL Data Definition Language (DDL)
and specify your anonymization policy inside the table definition itself.

%if %?postgresql_default
%description -n %{pkgname}
PostgreSQL Anonymizer is an extension to mask or replace
personally identifiable information (PII) or commercially sensitive data from
a PostgreSQL database.
The project has a declarative approach of anonymization. This means you can
declare the masking rules using the PostgreSQL Data Definition Language (DDL)
and specify your anonymization policy inside the table definition itself.
%endif


%prep
%autosetup -a1 -p1 -n %{extension}-%{version}
%{cargo_prep -v vendor}
echo "[patch.crates-io]
dunce = { path = 'vendor/dunce-1.0.5' }
constant_time_eq = { path = 'vendor/constant_time_eq-0.3.1' }
imgref = { path = 'vendor/imgref-1.11.0' }
" >> .cargo/config.toml


%build
# using normal cargo instead of the macros because `make extension` uses it too and needs to be able to find cargo pgrx
# cannot build all of pgrx since pgrx-pg-sys (and anonymizer) depends on `cargo pgrx init` being called first
export RUSTC_BOOTSTRAP=1
export RUSTFLAGS='%{build_rustflags}'
export CARGO_HOME=.cargo
export PGRX_HOME=%{_builddir}/.pgrx
cargo build %{?_smp_mflags} --profile rpm --manifest-path vendor/cargo-pgrx-%{pgrx_version}/Cargo.toml
mkdir .cargo/bin
cp vendor/cargo-pgrx-%{pgrx_version}/target/rpm/cargo-pgrx .cargo/bin
cargo pgrx init --pg%{pgversion} %{pg_config}
%make_build extension PG_CONFIG=%{pg_config} PGVER=pg%{pgversion}

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest


%install
export TARGET_DIR=target/release/anon-pg%{pgversion}/
export COMMON_SHAREDIR=$(%{pg_config} --sharedir)
export COMMON_PKGLIBDIR=$(%{pg_config} --pkglibdir)
mkdir -p %{?buildroot}$COMMON_SHAREDIR/extension %{?buildroot}$COMMON_PKGLIBDIR
# unfortunate hack around an impermissive makefile
%make_install PG_CONFIG=%{pg_config} PGVER=pg%{pgversion} \
PG_SHAREDIR=%{?buildroot}$COMMON_SHAREDIR PG_PKGLIBDIR=%{?buildroot}$COMMON_PKGLIBDIR \
TARGET_SHAREDIR=$TARGET_DIR$COMMON_SHAREDIR TARGET_PKGLIBDIR=$TARGET_DIR$COMMON_PKGLIBDIR


# integration tests (make installcheck) and pg_tests are impossible to run here since postgres hardcodes
# where it looks for extensions, and the pgrx_tests package also requires root access to be installed and run
# therefore, we can only run unit tests
%check
PGRX_HOME=%{_builddir}/.pgrx CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 RUSTFLAGS='%{build_rustflags}' cargo pgrx test -rv pg%{pgversion} ::test_


%files -n %{pkgname}
%{_libdir}/pgsql/anon.so
%{_datadir}/pgsql/extension/anon--%{version}.sql
%{_datadir}/pgsql/extension/anon.control
%{_datadir}/pgsql/extension/anon
%license LICENSE.md
%license LICENSE.dependencies
%license cargo-vendor.txt
# not copying the docs/ folder since it is too large and contains no manfiles
%doc AUTHORS.md CHANGELOG.md NEWS.md README.md


%changelog
%autochangelog
