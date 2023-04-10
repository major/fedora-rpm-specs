%global octpkg jsonlab

Name:           octave-%{octpkg}
Version:        2.0
Release:        10%{?dist}
Summary:        A JSON/UBJSON/MessagePack encoder/decoder for MATLAB/Octave
License:        GPLv3+ or BSD
URL:            http://openjdata.org/jsonlab
Source0:        https://github.com/fangq/jsonlab/archive/v%{version}/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave octave-zmat
Requires(post): octave
Requires(postun): octave

%description
JSONLab is a free and open-source implementation of a JSON/UBJSON/MessagePack 
encoder and a decoder in the native MATLAB language. It can be used to convert 
a MATLAB data structure (array, struct, cell, struct array and cell array) into
JSON/UBJSON formatted string, or decode a JSON/UBJSON/MessagePack file into 
MATLAB data. JSONLab supports both MATLAB and GNU Octave (a free MATLAB clone).
JSONLab is now the official reference implementation for the JData Specification 
(Draft 3) - the foundation of the OpenJData Project (http://openjdata.org).

%prep
%autosetup -n %{octpkg}-%{version}

cp LICENSE_GPLv3.txt COPYING

mkdir -p inst/
rm Contents.m
mv *.m inst/

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE_GPLv3.txt LICENSE_BSD.txt
%doc README.rst AUTHORS.txt ChangeLog.txt 
%doc examples
%doc test
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 2.0-10
- Rebuild with octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 2.0-7
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.0-5
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 13 2020 Qianqian Fang <fangqq@gmail.com> - 2.0-1
- Update to 2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Qianqian Fang <fangqq@gmail.com> - 1.9.8-2
- Update to re-released 1.9.8

* Thu Oct 24 2019 Qianqian Fang <fangqq@gmail.com> - 1.9.8-1
- Update to 1.9.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.8-4
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.8-2
- Rebuild for octave 4.4

* Sun Sep 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8-1
- Update to 1.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-1
- Update to 1.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.0-1
- Update to 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.0-2
- Remove svn files from doc

* Wed Nov 04 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.0-1
- Initial package
