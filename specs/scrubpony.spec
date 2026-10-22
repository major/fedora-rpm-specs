Name:           scrubpony
Version:        1.3.0
Release:        %{autorelease}
Summary:        Strip identifying metadata out of images without touching a single pixel

License:        MIT
URL:            https://github.com/norsehorse-dev/ScrubPony
Source0:        %{url}/archive/v%{version}/ScrubPony-%{version}.tar.gz 

BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
# Test requirements
BuildRequires:  libasan
BuildRequires:  libubsan
# Needed in tests that compare metadata removal
BuildRequires:  /usr/bin/exiftool
BuildRequires:  python3-pillow

%description
Strips identifying metadata out of images without touching a single pixel.

Lossless, no re-encoding, no quality loss, no dependencies beyond libc. C99,
macOS and Linux. Reads JPEG, PNG, WebP, and HEIC; drops whatever else it is
pointed at rather than guessing.

%prep
%autosetup -n ScrubPony-%{version}


%build
%make_build
help2man ./scrubpony > scrubpony.1

%install
PREFIX=%{_prefix} %make_install
install -Dm 0644 scrubpony.1 %{buildroot}%{_mandir}/man1/scrubpony.1

%check
make check

%files
%license LICENSE
%doc README.md
%{_bindir}/scrubpony
%{_mandir}/man1/scrubpony.1*

%changelog
%autochangelog
