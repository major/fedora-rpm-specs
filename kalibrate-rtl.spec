%global git_commit aae11c8a8dc79692a94ccfee39ba01e8c8c05d38
%global git_date 20141008
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             kalibrate-rtl
URL:              http://github.com/steve-m/kalibrate-rtl
Version:          0.4.1
Release:          20.%{git_suffix}%{?dist}
License:          BSD
BuildRequires:  gcc-c++
BuildRequires:    autoconf, automake, rtl-sdr-devel, fftw-devel
BuildRequires:    libusbx-devel
BuildRequires: make
Summary:          GSM based frequency calibration for rtl-sdr
Source0:          https://github.com/steve-m/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz


%description
Kalibrate, or kal, can scan for GSM base stations in a given frequency band and
can use those GSM base stations to calculate the local oscillator frequency
offset.

%prep
%setup -qn %{name}-%{git_commit}
autoreconf -fi

%build
%configure
make CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Rename kal to kal-rtl to avoid possible conflicts
mv %{buildroot}%{_bindir}/kal %{buildroot}%{_bindir}/kal-rtl

%files
%doc COPYING README AUTHORS
%{_bindir}/*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-20.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-19.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-18.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-16.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5.20141008gitaae11c8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.1-4.20141008gitaae11c8a
- Rebuilt for GCC 5 C++11 ABI change

* Tue Oct 14 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-3.20141008gitaae11c8a
- required libusbx-devel instead of libusb-devel

* Fri Oct 10 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-2.20141008gitaae11c8a
- Fixed source URL according to fedora review

* Wed Oct  8 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-1.20141008gitaae11c8a
- Initial release
