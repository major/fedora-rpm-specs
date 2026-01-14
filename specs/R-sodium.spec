Name:           R-sodium
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        A Modern and Easy-to-Use Crypto Library

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libsodium)

%description
Bindings to 'libsodium': a modern, easy-to-use software library for encryption,
decryption, signatures, password hashing and more. Sodium uses curve25519, a
state-of-the-art Diffie-Hellman function by Daniel Bernstein, which has become
very popular after it was discovered that the NSA had backdoored Dual EC DRBG.

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
