Name:           bitstream
Version:        1.6
Release:        %autorelease
Summary:        Simpler access to binary structures such as specified by MPEG, DVB, IETF

License:        MIT
URL:            https://code.videolan.org/videolan/bitstream
Source0:        http://download.videolan.org/pub/videolan/bitstream/%{version}/bitstream-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  make

%description
biTStream is a set of C headers allowing a simpler access to binary structures
such as specified by MPEG, DVB, IETF, etc.

%package devel
Summary: Simpler access to binary structures such as specified by MPEG, DVB, IETF

%description devel
biTStream is a set of C headers allowing a simpler access to binary structures
such as specified by MPEG, DVB, IETF, etc.


%prep
%autosetup -p1


%build
#Nothing to build


%install
%make_install PREFIX=%{_prefix}



%files devel
%doc AUTHORS NEWS README TODO
%license COPYING
%{_includedir}/bitstream
%{_datadir}/pkgconfig/bitstream.pc


%changelog
%autochangelog
