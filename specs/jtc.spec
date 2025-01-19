%define tag_name LatestBuild
Name:           jtc
Version:        1.76a
Release:        12%{?dist}
Summary:        JSON processing utility

License:        MIT
URL:            https://github.com/ldn-softdev/jtc
Source0:        %{URL}/archive/%{tag_name}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

%description
jtc stand for: JSON transformational chains (used to be JSON test console).

jtc offers a powerful way to select one or multiple elements from a source JSON
and apply various actions on the selected elements at once (wrap selected
elements into a new JSON, filter in/out, sort elements, update elements, insert
new elements, remove, copy, move, compare, transform, swap around and many other
operations).


%prep
%autosetup -n %{name}-%{tag_name}

%build
g++ -std=gnu++14 %build_cxxflags -pthread -lpthread %{name}.cpp -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md
%doc "User Guide.md"
%doc "Walk-path tutorial.md"

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.76a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.76a-1
- New upstream release 1.76a

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.75d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.75d-1
- New upstream release 1.75d

* Sun Jan 12 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.75c-1
- Initial package version
