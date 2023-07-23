%global commit 7f449bf8bd3b933891d12c30112268c4090e4d59
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20210312

Name:       rnnoise
Version:    0
Release:    0.8.%{date}git%{shortcommit}%{?dist}
Summary:    Recurrent neural network for audio noise reduction

# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/HB2GPMVKMTNP5WDGIRNU5NZUO4JWQPII/
License:    BSD

URL:        https://gitlab.xiph.org/xiph/rnnoise
Source0:    %{url}/-/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: make

%description
RNNoise is a noise suppression library based on a recurrent neural network.

While it is meant to be used as a library, a simple command-line tool is
provided as an example. It operates on RAW 16-bit (machine endian) mono PCM
files sampled at 48 kHz. It can be used as:

./examples/rnnoise_demo <noisy speech> <output denoised>

The output is also a 16-bit raw PCM file.


%package    devel
Summary:    Devel files for %{name}

Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for %{name}.


%prep
%autosetup -n %{name}-%{commit} -p1

cat > 'package_version' <<-EOF
    PACKAGE_VERSION=%{date}git%{shortcommit}
EOF


%build
./autogen.sh
%configure \
    --disable-static
%make_build


%install
%make_install
rm %{buildroot}%{_libdir}/*.la

# Duplicate
rm %{buildroot}%{_docdir}/%{name}/COPYING


%files
%license COPYING
%doc TRAINING-README AUTHORS README
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20210312git7f449bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20210312git7f449bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20210312git7f449bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20210312git7f449bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20210312git7f449bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.3.20210312git7f449bf
- build(update): 20210312git7f449bf

* Sun Jan 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20210122git1cbdbcf
- Initial package
