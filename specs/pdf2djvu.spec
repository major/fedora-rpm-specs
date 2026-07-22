Name:           pdf2djvu
Version:        0.9.19
Release:        %autorelease
Summary:        PDF to DjVu converter
License:        GPL-2.0-or-later
URL:            http://jwilk.net/software/pdf2djvu
Source0:        https://github.com/jwilk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:         pdf2djvu-poppler-version.patch
Patch1:         pdf2djvu-poppler-26.01.0.patch

ExcludeArch:    %{ix86}

BuildRequires:  djvulibre
BuildRequires:  djvulibre-devel
BuildRequires:  exiv2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  poppler-devel

Requires:       djvulibre

%description
pdf2djvu creates DjVu files from PDF files. It's able to extract:
graphics, text layer, hyperlinks, document outline (bookmarks) and
metadata.

%prep
%autosetup -p1

%build
export CXXFLAGS="%{optflags} -std=c++20"
%configure
%make_build

%install
%make_install
%find_lang %{name}

%check
%{buildroot}%{_bindir}/%{name} --version

%files -f %{name}.lang
%license doc/COPYING
%doc doc/README doc/changelog doc/credits
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/de/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_mandir}/pl/man1/%{name}.1*
%{_mandir}/pt/man1/%{name}.1*
%{_mandir}/ru/man1/%{name}.1*


%changelog
%autochangelog
