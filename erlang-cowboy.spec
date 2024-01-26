%global realname cowboy
%global upstream ninenines


Name:		erlang-%{realname}
Version:	2.7.0
Release:	11%{?dist}
BuildArch:	noarch
Summary:	Small, fast, modular HTTP server written in Erlang
License:	ISC
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-cowlib
BuildRequires:	erlang-ranch
BuildRequires:  erlang-rebar
# For building docs
BuildRequires:	asciidoc
BuildRequires:	dblatex
BuildRequires:	libxml2


%description
Small, fast, modular HTTP server written in Erlang.


%package doc
Summary: Documentation for %{name}


%description doc
Documentation for %{name}.


%prep
%autosetup -p 1 -n %{realname}-%{version}
# Better remove it entirely and add dependcy on js-jquery
sed -i 's/\r//' examples/websocket/priv/static/jquery.min.js

# FIXME temporary (until we'll have a Fedora JavaScript Packaging Guidelines) remove problematic examples
rm -rf examples/websocket


%build
%{erlang_compile}
# Building docs
# FIXME broken right now
#a2x -v -f pdf CONTRIBUTING.asciidoc
#a2x -v -f pdf doc/src/guide/book.asciidoc && mv doc/src/guide/book.pdf doc/guide.pdf
#a2x -v -f chunked doc/src/guide/book.asciidoc && mv doc/src/guide/book.chunked/ doc/html/
#for f in doc/src/manual/*.asciidoc ; do a2x -v -f manpage $f ; done


%install
%{erlang_install}

# man-pages installation
install -d %{buildroot}%{_mandir}/man3
install -d %{buildroot}%{_mandir}/man7
for manfile in `ls doc/src/manual/*.3`
do
	install -p -m 0644 $manfile %{buildroot}%{_mandir}/man3/
done
for manfile in `ls doc/src/manual/*.7`
do
	install -p -m 0644 $manfile %{buildroot}%{_mandir}/man7/
done


%check
# CT test-suite requires ct_helper, gun
#  https://github.com/ninenines/ct_helper
#  https://github.com/ninenines/gun
#%%{erlang_test}


%files
%license LICENSE
%doc README.asciidoc
%{erlang_appdir}/
#%%{_mandir}/man3/*
#%%{_mandir}/man7/*


#%%files doc
#%%doc CONTRIBUTING.pdf ROADMAP.md doc/guide.pdf doc/html examples/


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.7.0-1
- Ver. 2.7.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.4.0-1
- Ver. 2.4.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-1
- Ver. 2.0.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.4.pre.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.3.pre.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.2.pre.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 14 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.0-0.1.pre.3
- Ver. 2.0.0-pre.3
- Doc-subpackage no longer requires main package.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-4
- Remove dependency on _isa in *-doc sub-package

* Mon Mar 18 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-3
- Temporary remove one problematic example.

* Sun Mar 17 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-2
- Split-off doc subpackage

* Thu Mar 14 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-1
- Ver. 0.8.2

* Fri Jan 25 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.6.1-1
- Intial build
