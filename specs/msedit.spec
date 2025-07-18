# Partially generated by rust2rpm 27
%bcond check 1

# prevent library files from being installed
%global cargo_install_lib 0

# icu soversion
%global icu_sover 76
%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif

Name:           msedit
Version:        1.2.0
Release:        %autorelease
Summary:        Simple editor inspired by the MS-DOS Editor
SourceLicense:  MIT
# MIT OR Apache-2.0: libc v0.2.172
# MIT: edit v1.2.0
License:        MIT AND (MIT OR Apache-2.0)

URL:            https://github.com/microsoft/edit
Source:         %{url}/archive/v%{version}/edit-%{version}.tar.gz
Patch:          edit-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  libicu-devel

# For dlopen() libicu
Requires:       libicuuc.so.%{icu_sover}%{?lib64_suffix}
Requires:       libicui18n.so.%{icu_sover}%{?lib64_suffix}

%global _description %{expand:
%{summary}

A text editor that pays homage to the classic MS-DOS Editor, but with a modern
interface and input controls similar to VS Code. The goal is to provide an
accessible editor that even users largely unfamiliar with terminals can easily
use.
}

%description %{_description}

%prep
%autosetup -n edit-%{version} -p1

# Patch the code to load the correct icu libraries
# To avoid requiring the libicu-devel package at runtime
sed -i src/sys/unix.rs \
    -e "s/libicuuc.so/libicuuc.so.%{icu_sover}/g" \
    -e "s/libicui18n.so/libicui18n.so.%{icu_sover}/g"

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
# de-conflict with vim
mv %{buildroot}%{_bindir}/edit %{buildroot}%{_bindir}/%{name}

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%{_bindir}/%{name}

%changelog
%autochangelog
