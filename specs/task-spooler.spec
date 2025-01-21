Name:           task-spooler
Version:        1.0.2
Release:        8%{?dist}
Summary:        Personal job scheduler

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://vicerveza.homeunix.net/~viric/soft/ts
Source0:        %{url}/ts-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc

%description
Task spooler is a Unix batch system where the tasks spooled run one
after the other. Each user in each system has his own job queue. The tasks are
run in the correct context (that of enqueue) from any shell/process, and its
output/results can be easily watched. It is very useful when you know that
your commands depend on a lot of RAM, a lot of disk use, give a lot of
output, or for whatever reason it's better not to run them at the same time.

%prep
%autosetup -n ts-%{version}


%build
%set_build_flags
%make_build


%install
%make_install PREFIX=%{buildroot}%{_prefix}
mv %{buildroot}%{_bindir}/ts %{buildroot}%{_bindir}/tsp
mv %{buildroot}%{_mandir}/man1/ts.1 %{buildroot}%{_mandir}/man1/tsp.1


%files
%license COPYING
%doc Changelog README TRICKS PROTOCOL
%{_bindir}/tsp
%{_mandir}/man1/tsp.1.*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.2-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0-1
- Initial package for Fedora
