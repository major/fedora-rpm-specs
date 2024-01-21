%global realname amf
%global upstream mujaheed
%global git_tag 8fea004e61c746c16271476c190a9c01e398a2d5
%global short_tag %(c=%{git_tag}; echo ${c:0:7})


Name:		erlang-%{realname}
Version:	0
Release:	0.31.20110224git%{short_tag}%{?dist}
BuildArch:	noarch
Summary:	Erlang Action Message Format Library
License:	BSD
URL:		https://github.com/%{upstream}/erlang-%{realname}
VCS:		scm:git:https://github.com/%{upstream}/erlang-%{realname}.git
Source0:	https://github.com/%{upstream}/erlang-%{realname}/archive/%{git_tag}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar


%description
Erlang Action Message Format Library.


%prep
%setup -q -n erlang-%{realname}-%{git_tag}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%doc README doc
%{erlang_appdir}/


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20110224git8fea004
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Peter Lemenkov <lemenkov@gmail.com> - 0-0.20.20170825git8fea004
- Update to the latest git snapshot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 0-0.14.20110224gitb36dfb6
- Spec-file cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20110224gitb36dfb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Peter Lemenkov <lemenkov@gmail.com> - 0-0.6.20110224gitb36dfb6
- Updated to the next git tag and dropped upstreamed patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20100908git27329144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20100908git27329144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 31 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.3.20100908git27329144
- Fixed missing BIFs in Erlang/OTP R12B
- Exported one more function

* Wed Sep 22 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.2.20100908git27329144
- Narrow BuildRequires

* Wed Sep  8 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.20100908git27329144
- Initial build

