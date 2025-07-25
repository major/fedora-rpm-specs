# FIXME:  Figure out what to do about the gles* manpages, maybe different conflicting packages...
%global codate 20190306
%global commit 4547332f0f27d98601a8f5732ce8e85e09dbdb93
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gl-manpages
Version:        1.1
Release:        34.%{codate}%{?dist}
Summary:        OpenGL manpages

# This package uses SGI-B-1.1, we choose to use later variant of this license
# becase SGI-B-1.1 is not allowed, but it allows to use later variants and
# that is allowed
License:        Apache-2.0 AND HPND AND HPND-sell-variant AND MIT AND OpenPBS-2.3 AND SGI-B-2.0 AND W3C-19980720 AND X11
URL:            https://github.com/KhronosGroup/OpenGL-Refpages
Source0:        https://github.com/KhronosGroup/OpenGL-Refpages/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# FIXME: Bundle mathml and the Oasis dbmathl until they are packaged
Source2:        http://www.oasis-open.org/docbook/xml/mathml/1.1CR1/dbmathml.dtd
Source3:        http://www.w3.org/Math/DTD/mathml2.tgz
# FIXME  These are the old gl-manpages source which 
# still have some manpages that khronos doesn't. 
# Ship until somebody in the know helps figuring whats what.
# When matching install the khronos version.
Source4:        gl-manpages-1.0.1.tar.bz2
#Silence author/version/manual etc. warnings
Source5:        metainfo.xsl

BuildArch:      noarch

BuildRequires: make
BuildRequires:  libxslt docbook-style-xsl docbook5-style-xsl python3

%description
OpenGL manpages

%prep
%setup -q -n OpenGL-Refpages-%{commit}
tar xzf %{SOURCE3}
cp -av %{SOURCE2} mathml2/
tar xjf %{SOURCE4}


%build
export BD=`pwd`
xmlcatalog --create --noout \
	--add public "-//W3C//DTD MathML 2.0//EN" "file://$BD/mathml2/mathml2.dtd" \
	--add system "http://www.w3.org/TR/MathML2/dtd/mathml2.dtd" "file://$BD/mathml2/mathml2.dtd" \
	--add public "-//OASIS//DTD DocBook MathML Module V1.1b1//EN" "file://$BD/mathml2/dbmathml.dtd" \
	--add system "http://www.oasis-open.org/docbook/xml/mathml/1.1CR1/dbmathml.dtd" "file://$BD/mathml2/dbmathml.dtd" \
	mathml2.cat
export XML_CATALOG_FILES="$BD/mathml2.cat /etc/xml/catalog"
make
pushd gl4
	for MANP in gl*.xml ; do
		xsltproc --xinclude --nonet %{SOURCE5} $MANP | xsltproc --xinclude --nonet /usr/share/sgml/docbook/xsl-ns-stylesheets/manpages/docbook.xsl -
	done
popd


%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
cp -n gl4/*.3G $RPM_BUILD_ROOT%{_mandir}/man3/
# install the old manpages source with 3gl -> 3G
# when matchin don't clobber the khronos version
for MANP in `find gl-manpages-1.0.1 -name *.3gl` ; do
	FN=${MANP//*\//}
	cp -a --update=none $MANP $RPM_BUILD_ROOT%{_mandir}/man3/${FN/.3gl/.3G}
done
find $RPM_BUILD_ROOT%{_mandir}/man3/ -type f -size -100b | xargs sed -i -e 's/\.3gl/\.3G/' -e 's,^\.so man3G/,.so man3/,'


%files
%{_mandir}/man3/*


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-34.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-33.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-32.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 07 2023 José Expósito <jexposit@redhat.com> - 1.1-29.20190306
- SPDX Migration

* Thu Jul 20 2023 Yanko Kaneti <yaneti@declera.com> - 1.1-28.20190306
- Adjust for recent changes in behavior in coreutils cp --no-clobber

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19.20190306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar  6 2019 Yanko Kaneti <yaneti@declera.com> - 1.1-18.20190306
- Switch to the new upstream github repo sources
- Build only gl4 manpages for now

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17.20161227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16.20161227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15.20161227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14.20161227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13.20161227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Yanko Kaneti <yaneti@declera.com> - 1.1-12.20161227
- Use docbook5-style-xsl for building the GL4 manpages

* Tue Dec 27 2016 Yanko Kaneti <yaneti@declera.com> - 1.1-11.20161227
- New upstream snapshot.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11.20140424
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10.20140424
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9.20140424
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Yanko Kaneti <yaneti@declera.com> - 1.1-8.%{codate}
- New upstream snapshot
- GLSL folded into man4.
- tarball tweaks

* Tue Nov  5 2013 Yanko Kaneti <yaneti@declera.com> - 1.1-7.%{codate}
- New upstream snapshot.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7.20130122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6.20130122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Yanko Kaneti <yaneti@declera.com> - 1.1-5.%{codate}
- Newer upstream snapshot. Minor upstream rearrangement.
- Remove checkout script from sources and add to git.
- Try to actually use the bundled mathml2. Fix warnings.

* Wed Jan 16 2013 Yanko Kaneti <yaneti@declera.com> - 1.1-4.%{codate}
- Fix symlinked man references some more (#895986) 

* Mon Oct 15 2012 Yanko Kaneti <yaneti@declera.com> - 1.1-3.%{codate}
- Fix symlinked man variants. 
- Preserve timestamps on the older gl-manpages.

* Tue Oct  9 2012 Yanko Kaneti <yaneti@declera.com> - 1.1-2.%{codate}
- Re-add the older gl-manpages for those not present in khronos

* Tue Oct  9 2012 Yanko Kaneti <yaneti@declera.com> - 1.1-1.%{codate}
- Try building from source

* Wed Sep  5 2012 Yanko Kaneti <yaneti@declera.com> - 1.0.1-1
- Initial split from mesa
