# the tar file from the git sources is created with a script that executes
# the following commands:

#GITHUB_USER=supernovus
#SOFTWARE=exemel
#GIT_SRC_DIR=${SOFTWARE}-0.0.3
#
#URL=https://github.com/${GITHUB_USER}/${SOFTWARE}.git
#
#echo "creating tar archive from git sources"
#echo
#
#rm -rf ${SOFTWARE} ${SOFTWARE}-0.*
#git clone ${URL}
#
#rm -f $GIT_SRC_DIR
#ln -s $SOFTWARE $GIT_SRC_DIR
#tar --exclude="$GIT_SRC_DIR/.git" -czvhf ${GIT_SRC_DIR}.tar.gz ${GIT_SRC_DIR}/
#
#echo
#echo "done"


Name:		rakudo-XML
Version:	0.0.3
Release:	0.12.20190728git417f637%{?dist}
Summary:	An Object-Oriented XML Library for Perl 6 

License:	Artistic 2.0
URL:		https://github.com/supernovus/exemel
Source0:	ftp://ftp.uni-siegen.de/pub/Perl6Mod.src/exemel-%{version}.tar.gz

BuildRequires:	perl-interpreter, perl-Test-Harness
BuildRequires:	rakudo >= %rakudo_rpm_version
Requires:	rakudo >= %rakudo_rpm_version


%description
XML (originally called Exemel) is a full fledged XML library for Perl 6.

It handles parsing, generating, manipulating and querying XML. It supports
element queries, parent element information, namespaces, and an extendable
interface.

It supports every major kind of XML Node (XML::Node):

    - Document (XML::Document)
    - Element (XML::Element)
    - Text (XML::Text)
    - Comment (XML::Comment)
    - PI (XML::PI)
    - CDATA (XML::CDATA)

You can easily serialize the objects back to XML text by using any XML::Node
object in a string context.


%prep
%setup -q -n exemel-%{version}


%install
export QA_SKIP_BUILD_ROOT=1
RAKUDO_RERESOLVE_DEPENDENCIES=0 %perl6_mod_inst --to=%{buildroot}%{perl6_vendor_dir} --for=vendor


%check
prove -e 'perl6 -Ilib' t


%files
%doc README.md
%license LICENSE
%{perl6_vendor_dir}/*/*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-0.12.20190728git417f637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-0.11.20190728git417f637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-0.10.20190728git417f637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-0.9.20190728git417f637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-0.8.20190728git417f637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-0.7.20190728git417f637
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.3-0.6.20190728git417f637
- update source to current git repository
- add QA_SKIP_BUILD_ROOT=1
- remove exclulde of s390x and ppc64 architectures

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-0.5.20170930git420bf9c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-0.4.20170930git420bf9c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 30 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.3-0.1.20170930git420bf9c
- create initial spec file
