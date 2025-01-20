%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname fontquery
%global _description %{expand:
%{srcname} is a toolset to query/compare fonts for Fedora.
}

Name:           python-%{srcname}
Version:        1.21
Release:        3%{?dist}
Summary:        Font Querying tool for Fedora
License:        MIT
URL:            https://github.com/fedora-i18n/fontquery
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-wheel
BuildRequires:	python%{python3_pkgversion}-termcolor

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary: Pyrthon library for Font Querying tool

%description -n python%{python3_pkgversion}-%{srcname} %_description

This package contains Python library for %{srcname}.

%package -n %{srcname}
Summary: %{summary}
Requires: python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
Requires: fontconfig git-core
Obsoletes: %{srcname}-builder < 1.8-2
Recommends: podman

%description -n %{srcname} %_description

This package contains the end-user executables for %{srcname}.

%package -n %{srcname}-builder
Summary: Image build tools for Font Querying tool
Requires: python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
Requires: buildah podman

%description -n %{srcname}-builder %_description

This package contains the image build tools for %{srcname}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n %{srcname}
%license LICENSE
%doc README.md
%{_bindir}/fontquery
%{_bindir}/fontquery-client
%{_bindir}/fontquery-diff
%{_bindir}/fq2html

%files -n %{srcname}-builder
%license LICENSE
%doc README.md
%{_bindir}/fontquery-build

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 11 2024 Akira TAGOH <tagoh@redhat.com> - 1.21-2
- Add missing dependency of git-core.

* Tue Sep 10 2024 Akira TAGOH <tagoh@redhat.com> - 1.21-1
- New upstream release.

* Mon Sep  2 2024 Akira TAGOH <tagoh@redhat.com> - 1.20-1
- New upstream release.

* Fri Aug 30 2024 Akira TAGOH <tagoh@redhat.com> - 1.16-1
- New upstream release.

* Mon Aug 26 2024 Akira TAGOH <tagoh@redhat.com> - 1.14-1
- New upstream release.

* Fri Aug 02 2024 Adam Williamson <awilliam@redhat.com> - 1.13-4
- Backport PR #5 to exit 1 on diff as well as missing

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.13-2
- Rebuilt for Python 3.13

* Fri May 10 2024 Akira TAGOH <tagoh@redhat.com> - 1.13-1
- New upstream release.

* Wed May  8 2024 Akira TAGOH <tagoh@redhat.com> - 1.12-1
- New upstream release.
- Add fontconfig as a dependency.
  Resolves: rhbz#2278116

* Mon Mar 25 2024 Akira TAGOH <tagoh@redhat.com> - 1.10-1
- New upstream release.

* Mon Mar 11 2024 Akira TAGOH <tagoh@redhat.com> - 1.9-1
- New upstream release.

* Mon Mar  4 2024 Akira TAGOH <tagoh@redhat.com> - 1.8-2
- Move fontquery-container from fontquery-builder to fontquery package.
  Resolves: rhbz#2267616
- Add podman as Recommends to fontquery.
- Add podman and buildah as Requires to fontquery-builder.

* Thu Feb  1 2024 Akira TAGOH <tagoh@redhat.com> - 1.8-1
- New upstream release.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Akira TAGOH <tagoh@redhat.com> - 1.6-1
- New upstream release.

* Mon Sep  4 2023 Akira TAGOH <tagoh@redhat.com> - 1.4-1
- Initial packaging.
