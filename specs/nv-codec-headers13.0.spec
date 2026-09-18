Name:           nv-codec-headers13.0
Epoch:           1
Version:        13.0.19.1
Release:        %autorelease
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
Source0:        %{url}/archive/n%{version}/nv-codec-headers-n%{version}.tar.gz

BuildArch:      noarch
Conflicts:      nv-codec-headers

BuildRequires:  make

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.


%prep
%autosetup -n nv-codec-headers-n%{version}
sed -i -e 's@/include@/include/ffnvcodec@g' ffnvcodec.pc.in

# Extract license
sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE
sed -i '1,22s/^.\{,3\}//' LICENSE

%build
%make_build PREFIX=%{_prefix} LIBDIR=/share


%install
%make_install PREFIX=%{_prefix} LIBDIR=/share


%files
%doc README
%license LICENSE
%{_includedir}/ffnvcodec/
%{_datadir}/pkgconfig/ffnvcodec.pc


%changelog
%autochangelog
