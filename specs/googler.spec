Name:       googler
Version:    4.3.2
Release:    11%{?dist}
Summary:    Access google search, google site search, google news from the terminal

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://github.com/jarun/googler
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make


%description
googler is a power tool to access Google (Web & News) websites and Google Site
Search website from the command-line. It shows the title, URL and abstract
for each result, which can be directly opened in a browser from the terminal.
Results are fetched in pages (with page navigation). Supports sequential
searches in a single googler instance.

googler was initially written to cater to headless servers without X. You can
integrate it with a text-based browser. However, it has grown into a very handy
and flexible utility that delivers much more. For example, fetch any number of
results or start anywhere, limit search by any duration, define aliases to
google search any number of websites, switch domains easily... all of this
in a very clean interface without ads or stray URLs. The shell completion
scripts make sure you don't need to remember any options.

googler isn't affiliated to Google in any way.


%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' googler


%build
make disable-self-upgrade


%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/googler-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/googler.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_googler


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/googler-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/googler.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_googler


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.2-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar  7 10:55:05 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 4.3.2-1
- Update to 4.3.2
- Close: rhbz#1918769

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 12:55:55 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.3.1-1
- Release 4.3.1 (close: #1887051)

* Mon Aug 24 17:40:57 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.2-1
- Release 4.2 (#1861154)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 23:28:58 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.1-1
- Release 4.1 (#1830152)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 21:54:30 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.0-1
- Release 4.0 (#1777084)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 14:45:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.9-1
- Release 3.9 (#1715305)

* Wed Mar 27 16:11:44 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.8-1
- Release 3.8 (#1693334)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.7.1-1
- Release 3.7.1

* Sun Sep 16 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.7-1
- Release 3.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.6-1
- Release 3.6

* Sat Feb 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.5-1
- First RPM release
