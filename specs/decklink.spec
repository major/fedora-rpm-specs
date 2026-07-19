Name:           decklink
Version:        16.0
Release:        %autorelease
Summary:        BlackMagic Design SDK for DeckLink

License:        BSL-1.0
URL:            https://www.blackmagicdesign.com/desktopvideo_sdk
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-tarball.sh

BuildArch:      noarch

%description
This is a bare version of the DeckLink SDK from BlackMagic Design. The
original, fully featured with examples, can be found at
https://www.blackmagicdesign.com/desktopvideo_sdk

The C++ Header and Source files are licensed under the Boost License
with the copyright owned by BlackMagic Design. This license is an OSI
approved MIT-like and compatible with the GPLv2.

%package devel
Summary: BlackMagic Design SDK for DeckLink - header files
Provides: %{name}-static = %{version}-%{release}

%description devel
This is a bare version of the DeckLink SDK from BlackMagic Design. The
original, fully featured with examples, can be found at
https://www.blackmagicdesign.com/desktopvideo_sdk

The C++ Header and Source files are licensed under the Boost License
with the copyright owned by BlackMagic Design. This license is an OSI
approved MIT-like and compatible with the GPLv2.

%prep
%autosetup

%build

%install
install -d %{buildroot}%{_includedir}/decklink
install -pm644 Linux/include/*.{h,cpp} %{buildroot}%{_includedir}/decklink

%files devel
%dir %{_includedir}/decklink
%{_includedir}/decklink/DeckLinkAPI*.h
%{_includedir}/decklink/DeckLinkAPIDispatch*.cpp
%{_includedir}/decklink/LinuxCOM.h

%changelog
%autochangelog
