Summary: Translate Dalvik bytecode to equivalent Java bytecode
Name: enjarify
Version: 1.0.3
Release: 25%{?dist}
License: ASL 2.0
URL: https://github.com/Storyyeller/enjarify
# Upstream uses gitattribues to remove test files from archive…
# git clone https://github.com/Storyyeller/enjarify
%if 0
(cd enjarify && rm .gitattributes && git commit -a -m 'Drop gitattributes' && git archive --prefix enjarify-%{version}/ -o ../enjarify-%{version}.tar.xz HEAD)
%endif
Source0: enjarify-%{version}.tar.xz
Source1: https://anonscm.debian.org/cgit/android-tools/enjarify.git/plain/debian/enjarify.1
# https://github.com/Storyyeller/enjarify/pull/1
Patch1:  0001-Adjust-test2-to-pass.patch
# https://github.com/Storyyeller/enjarify/pull/2
Patch2:  0002-runtests-drop-Xss-param.patch

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

# this package support python3 only
BuildRequires: python3-devel

# for %%check
BuildRequires: java-headless

Requires: python3-enjarify = %{version}-%{release}

%global _description %{expand:
Android applications are Java programs that run on a customized
virtual machine, which is part of the Android operating system, the
Dalvik VM. Their bytecode differs from the bytecode of normal Java
applications.

Enjarify can translate the Dalvik bytecode back to equivalent Java
bytecode, which simplifies the analysis of Android applications.}

%description %_description

%package -n python3-enjarify
Summary: %summary
%{?python_provide:%python_provide python3-enjarify}

%description -n python3-enjarify %_description

# No python2 support:
# https://github.com/google/enjarify/issues/11

%prep
%autosetup -n enjarify-%{version} -p1

%build
# nothing to do, package has no build system

%install
mkdir -p %buildroot%python3_sitelib \
         %buildroot%_bindir
cp -ap enjarify %buildroot%python3_sitelib/
rm %buildroot%python3_sitelib/enjarify/runtests.py

cat >%buildroot%_bindir/enjarify <<EOF
#!/bin/sh -e
exec %{__python3} -O -m enjarify.main "\$@"
EOF
chmod +x %buildroot%_bindir/enjarify

install -pDm0644 -t %buildroot%_mandir/man1/ %SOURCE1

%check
export PYTHONPATH=. LC_CTYPE="C.UTF-8"
%__python3 -m enjarify.runtests

# show help output to check that the script isn't totally broken
%buildroot%_bindir/enjarify --help

%files
%_bindir/enjarify
%_mandir/man1/enjarify.1*

%files -n python3-enjarify
%python3_sitelib/enjarify
%license LICENSE.txt
%doc README.md

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.3-25
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.3-22
- Rebuilt for Drop i686 JDKs

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.3-21
- Rebuilt for Python 3.11

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.3-20
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.3-17
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-15
- Enable tests (#1808128)

* Wed Aug 26 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-14
- Disable tests (#1808128). The tests are right and the package is broken
  with python3.9 (https://bugs.python.org/issue41531). Hopefully python3.9
  will be fixed before the final release.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-12
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-9
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-2
- Fix launcher script

* Thu Feb 23 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-1
- Add missing %%dist tag.
- Update URL to a new repo
- Use a custom tarball which contains tests/
- Add %%check

* Tue Feb  7 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-1
- Rename package to enjarify
- Add python3-enjarify subpackage
- Preserve timestamp of man page on installation and drop %%doc
- Use %%python_provide

* Fri Jan 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-1
- Initial packaging
