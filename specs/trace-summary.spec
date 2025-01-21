Name:           trace-summary
Version:        0.92
Release:        11%{?dist}
Summary:        Script generating break-downs of network traffic

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/zeek/trace-summary
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       pysubnettree

%description
trace-summary is a Python script that generates break-downs of network traffic,
including lists of the top hosts, protocols, ports, etc. Optionally, it can
generate output separately for incoming vs. outgoing traffic, per subnet, and
per time-interval.

%prep
%autosetup

%build
# nothing

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc CHANGES README
%license COPYING
%{_bindir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.92-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021  Fabian Affolter <mail@fabian-affolter.ch> - 0.92-2
- Remove shebang update

* Tue Mar 02 2021  Fabian Affolter <mail@fabian-affolter.ch> - 0.92-1
- Update to latest upstream release 0.92

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.91-1
- Update to latest upstream release 0.91

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.89-1
- Update URLs
- Update to latest upstream release 0.89

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.87-2
- Rebuilt for Python 3.7

* Sun Jul 01 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.87-1
- Update to latest upstream release 0.87

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.86-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.86-2
- Update shebang

* Sun Dec 25 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.86-1
- Update to latest upstream release 0.86

* Tue Aug 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.84-4
- Update for py3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.84-1
- Update to latest upstream release 0.84

* Fri Jun 20 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.83-1
- Initial package
