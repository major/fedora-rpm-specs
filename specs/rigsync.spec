%global git_commit b320c4d9a3ced9529391ac969cc29ff63f1c523a
%global git_date 20230612

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		rigsync
Version:	0~%{git_suffix}
Release:	7%{?dist}
Summary:	Rigsync keeps multiple rigs frequency and mode in sync using Hamlib
License:	LGPL-2.1-only
URL:		https://github.com/daveriesz/%{name}
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz

ExcludeArch:    i686

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	coreutils
BuildRequires:	hamlib-devel

%description
Rigsync is a utility that keeps the frequency and mode of multiple radios in
sync. Supported radios are all those supported by whatever version of
Hamlib to which rigsync is linked.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
%make_build CFLAGS="%{build_cflags} -DDEBUG" LDFLAGS="%{build_ldflags} -lhamlib"

%install
install -Dp %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/rigsync

%changelog
* Thu Feb 06 2025 Richard Shaw <hobbes1069@gmail.com> - 0~20230612gitb320c4d9-7
- Rebuild for hamlib 4.6.

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~20230612gitb320c4d9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 0~20230612gitb320c4d9-5
- Rebuild for Hamlib 4.6.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~20230612gitb320c4d9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~20230612gitb320c4d9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~20230612gitb320c4d9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0-20230612gitb320c4d9-1
- Initial version
