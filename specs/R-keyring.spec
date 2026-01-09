Name:           R-keyring
Version:        %R_rpm_version 1.4.1
Release:        %autorelease
Summary:        Access the System Credential Store from R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libsecret-1)

%description
Platform independent API to access the operating system's credential store.
Currently supports: Keychain on macOS, Credential Store on Windows, the Secret
Service API on Linux, and a simple, platform independent store implemented with
environment variables. Additional storage back-ends can be added easily.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
