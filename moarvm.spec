%global year 2020
%global month 07


Name:           moarvm
Version:        0.%{year}.%{month}
Release:        7%{?dist}
Summary:        Meta-model On A Runtime Virtual Machine

License:        Artistic 2.0
URL:            http://moarvm.org
Source0:        http://moarvm.org/releases/MoarVM-%{year}.%{month}.tar.gz
Patch0:         moarvm-probe-c99.patch

BuildRequires: make
# sha-devel
%if 0%{?fedora}
BuildRequires:  libatomic_ops-devel >= 7.4
#BuildRequires:  libtommath-devel >= 1.2
%endif

BuildRequires:  libffi-devel
BuildRequires:  libuv-devel

BuildRequires:  perl(Pod::Usage) perl(ExtUtils::Command) perl(autodie)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(FindBin)
#
%if 0%{?fedora}
BuildRequires:  discount
%%else
BuildRequires:  python3-markdown
%endif
BuildRequires:  gcc

Provides:       bundled(libtommath) = 1.2


%description
Short for "Metamodel On A Runtime", MoarVM is a virtual machine built
especially for Rakudo Perl 6 and the NQP Compiler Toolchain. MoarVM is a 
back-end for NQP.
MoarVM already stands out among the various Rakudo and NQP compilation
targets by typically:

    Running the Perl 6 specification test suite fastest
    Having the lowest memory usage
    Having the best start-up time
    Being fastest to build both NQP and Rakudo - and thus in theory your
        Perl 6 and NQP programs too!


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
This package contains header files for developing applications that use
%{name} (Metamodel On A Runtime).



%prep
%autosetup -p1 -n MoarVM-%{year}.%{month}


%build
# make sure to not bundle this
rm -r 3rdparty/msinttypes 3rdparty/libuv
# 3rdparty/sha1
# NQP do not build if MoarVM do not bundles sha

%if 0%{?fedora}
rm -r 3rdparty/libatomicops
rm -r 3rdparty/dyncall
#rm -r 3rdparty/libtommath
%endif

# Disable package-notes because its linker flag leaks to rakudo, bug #2070099
%undefine _package_note_file

# --has-sha \
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%{__global_ldflags}" perl ./Configure.pl \
  --prefix=%{_usr} --libdir=%{_libdir} --has-libuv --has-libffi \
%if 0%{?fedora}
  --has-libatomic_ops # --lua=%%{_bindir}/lua
# --has-libtommath
%endif

%{make_build} NOISY=1

# Generate HTML files
for F in docs/*.markdown docs/*.md
do
%if 0%{?fedora}
   discount-mkd2html $F
%else
   markdown_py-3 $F
%endif
done


%install
%make_install

# Force permissions on shared versioned libs so they get stripped
# and will provided.
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libmoar.so

# Generating man-page
%{__perl} -MExtUtils::Command -e mkpath $RPM_BUILD_ROOT%{_mandir}/man1
pod2man --section=1 --name=moar docs/moar.pod | %{__gzip} -c > $RPM_BUILD_ROOT%{_mandir}/man1/moar.1.gz


%files
%license LICENSE
%doc CREDITS docs
%{_bindir}/moar

%{_datadir}/nqp
# /usr/share/nqp/lib/MAST

%{_libdir}/libmoar.so

%{_mandir}/man1/moar.1.gz


%files devel
%{_includedir}/moar
%{_datadir}/pkgconfig/moar.pc

# EPEL
%if 0%{?rhel}
%{_includedir}/libatomic_ops
%endif

%exclude %{_includedir}/libtommath



%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Petr Pisar <ppisar@redhat.com> - 0.2020.07-6
- Disable package-notes (bug #2070099)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 0.2020.07-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2020.07-1
- update to 2020.07

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2020.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2020.02-1
- update to 2020.02

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2019.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2019.11-1
- update to 2019.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2019.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2019.03-1
- update to 2019.03

* Mon Oct 29 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2018.10-1
- update to 2018.10
- add BuildRequires perl(Data::Dumper)

* Mon Apr 30 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2018.04.1-1
- update to 2018.04.1, that fix denormals and precision issues in Num parser
- include the libatomic_ops header files, which are needed for EPEL

* Wed Apr 25 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2018.04-1
- update to 2018.04
- change the remove of the libatomic_ops sources to the new different directory

* Mon Aug 21 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.08.1-1
- change the work around of libtommath and add the definition of
  'MP_GEN_RANDOM_MAX'
- update to 2017.08.1

* Sun Jun 18 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.06-1
- use the environment variables CFLAGS and LDFLAGS
- update to 2017.06

* Mon May 08 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.04-2
- add $RPM_OPT_FLAGS to cflags again (bug #1448686)

* Fri Apr 28 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2017.04-1
- use the option has-libffi
- update to 2017.04

* Fri Dec 09 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2016.11-1
- build on epel7
- update to 2016.11

* Fri Jan 29 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2016.01-1
- sha1, msinttypes and tinymt header files will no longer installed
- update to 2016.01

* Fri Jun 19 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2015.06-1
- add HTML files and man-page generation
- change Summary text
- update to 2015.06

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2015.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 23 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2015.05-1
- 3rdparty/linenoise is gone, no readline are used
- update to 2015.05

* Sat Apr 25 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2015.04-2
- change MoarVM build to that NQP builds on top

* Sat Apr 25 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2015.04-1
- update to 2015.04

* Sat Jan 24 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.12-1
- update to 2014.12
- add pkgconfig/moar.pc file
- --libdir option could used

* Thu Jan 22 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.04-6
- add BuildRequies: perl(ExtUtils::Command) perl(autodie)
- rebuild to solve dependency

* Fri Aug 29 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.04-5
- remove of libtommath 3rdparty source files
- remove of libatomic_ops only if fedora > 20

* Fri Aug 22 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.04-4
- add 'BuildRequires: libatomic_ops-devel >= 7.4'
- first remove of 3rdparty source files

* Wed May 07 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.04-3
- modify Configure.pl so that the Fedora specific flags for cflags and ldflags
  will be written to the Makefile
- make lib64 directory creation more general

* Wed Apr 30 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.04-2
- add optimize flag to Configure.pl
- add CFLAGS and LDFLAGS to make
- change summary tag

* Sat Apr 26 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.04-1
- update to 2014.04
- remove patches that are included in upstream
- add BuildRequires perl(Pod::Usage)

* Mon Mar 31 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.03-2
- add patch to have more configuration flags
- call Confiugre.pl with has-libatomic_ops

* Wed Mar 26 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.03-1
- update to 2014.03
- call Configure.pl with has-sha and add BuildRequires sha-devel
- call Configure.pl with has-libuv and add BuildRequires libuv-devel
- exclude libuv and sha1 header file
- exclude header files for Microsoft Visual Studio (msinittypes)

* Mon Mar 17 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.02-3
- call Configure.pl with use-readline flag
- add BuildRequires readline-devel and libtommath-devel
- exclude linenoise and libtommath header file
- add patch to link with libtommath from the system and use it as a flag

* Fri Mar 14 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.02-2
- improve devel package tags
- description is no longer than 80 chars per line any more
- RPM_BUILD_ROOT cleanup is removed

* Sat Feb 22 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2014.02-1
- create initial spec file from the template 'rpmdev-newspec moarvm' 
- add changing permission of libmoar.so
- add Group tag
- add devel-subpackage
