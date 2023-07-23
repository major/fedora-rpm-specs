%global codate 20230721
%global commit0 7e127fee6a3981f6b0a50ce9910267cd501e09d4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global gitrev ff8e759
%global checkout 20110830git%{gitrev}

Name:           abootimg
Version:        0.6
Release:        %autorelease -s %{codate}git%{shortcommit0}
Summary:        Tool for manipulating Android boot images

License:        GPL-2.0-or-later
URL:            https://github.com/ggrandou/abootimg
Source0:        https://github.com/ggrandou/abootimg/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz

BuildRequires:  gcc
BuildRequires:  libblkid-devel

%description
abootimg is used to manipulate block devices or files with the special 
partition format defined by the Android Open Source Project.


%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
echo "#define VERSION_STR \"%{version}\"" > version.h
gcc ${RPM_OPT_FLAGS} -DHAS_BLKID -lblkid abootimg.c -o abootimg


%install
install -D abootimg ${RPM_BUILD_ROOT}/%{_bindir}/abootimg
install -D -m 644 -p debian/abootimg.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/abootimg.1


%files
%doc Changelog README
%license LICENSE
%{_bindir}/abootimg
%{_mandir}/man1/*


%changelog
%autochangelog
