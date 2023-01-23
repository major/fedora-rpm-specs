Name:           taskopen
Version:        1.1.5
Release:        5%{?dist}
Summary:        Script for taking notes and open urls with taskwarrior

License:        GPLv2+
URL:            https://github.com/ValiValpas/taskopen
Source0:        https://github.com/ValiValpas/taskopen/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires: perl-generators

Requires:       task

%description
taskopen allows you to link almost any file, webpage or command to a
taskwarrior task by adding a filepath, web-link or uri as an annotation. Text
notes, images, PDF files, web addresses, spreadsheets and many other types of
links can then be filtered, listed and opened by using taskopen. Some actions
are sane defaults, others can be custom-configured, and everything else will
use your systems mime-types to open the link.

Arbitrary commands can be used with taskopen at the CLI, acting on the link
targets, enhancing listings and even executing annotations as commands.

Run 'taskopen -h' or 'man taskopen' for further details. The following sections
show some (very) basic usage examples.

%prep
%autosetup

# Left overs?
rm -vf doc/html/*.orig


%build
# Nothing to do here


%install
%make_install PREFIX=%{_prefix}

# Wrong location, we'll intall it ourselves
rm -rfv $RPM_BUILD_ROOT/%{_datadir}/taskopen/doc


%files
%doc examples doc/html/
%{_bindir}/%{name}
%{_mandir}/man1/taskopen.1*
%{_mandir}/man5/taskopenrc.5*
%{_datadir}/%{name}/

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Jan Staněk <jstanek@redhat.com> - 1.1.5-1
- Update to version 1.1.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.4-1
- Initial build
- Update as per review comments: https://bugzilla.redhat.com/show_bug.cgi?id=1743802
