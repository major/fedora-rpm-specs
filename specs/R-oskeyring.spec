Name:           R-oskeyring
Version:        %R_rpm_version 0.1.6
Release:        %autorelease
Summary:        Raw System Credential Store Access from R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Aims to support all features of the system credential store, including non-
portable ones. Supports Keychain on macOS, and Credential Manager on
Windows. See the keyring package if you need a portable API.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
