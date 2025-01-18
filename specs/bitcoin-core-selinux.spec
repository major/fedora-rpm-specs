%global commit0 450561671211f8421c696ade1098d2b0a71b5fe8
%global date 20231127
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global selinuxtype targeted
%global modulename bitcoin

Name:           bitcoin-core-selinux
Version:        0^%{date}git%{shortcommit0}
Release:        17%{?dist}
Summary:        Bitcoin Core SELinux policy
License:        GPL-3.0-only
URL:            https://github.com/scaronni/%{name}
BuildArch:      noarch

Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
%{?selinux_requires}

%description
Bitcoin Core SELinux policy.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp

%install
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%pre
%selinux_relabel_pre -s %{selinuxtype}

%post
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
if %{_sbindir}/selinuxenabled ; then
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 8332
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 8333
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 8334
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 18332
     %{_sbindir}/semanage port -a -t %{modulename}_port_t -p tcp 18333
fi

%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi
if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 8332
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 8333
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 8334
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 18332
    %{_sbindir}/semanage port -d -t %{modulename}_port_t -p tcp 18333
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}

%files
%license LICENSE
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20231127git4505616-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Simone Caronni <negativo17@gmail.com> - 0^20231127git4505616-16
- Convert to new snapshot format.

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0-15.20231127git4505616
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20231127git4505616
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20231127git4505616
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20231127git4505616
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Simone Caronni <negativo17@gmail.com> - 0-11.20231127git4505616
- Update policies (#2246255).

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20210312giteaa9a04
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20210312giteaa9a04
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20210312giteaa9a04
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 0-7.20210312giteaa9a04
- Do not use forge macros. Breaks changelog, date in package release, changelog
  and complete release on EPEL 8.

* Wed Sep 22 2021 Simone Caronni <negativo17@gmail.com> - 0-6
- Rename to bitcoin-core-selinux.

* Sun Mar 14 2021 Simone Caronni <negativo17@gmail.com> - 0-5
- Use forge macros from packaging guidelines.

* Fri Mar 12 2021 Simone Caronni <negativo17@gmail.com> - 0-4.20210312giteaa9a04
- Updated policy.

* Fri Mar 12 2021 Simone Caronni <negativo17@gmail.com> - 0-3.20210312git7d10d99
- Allow connections to tor ports, remove permissive.

* Fri Mar 12 2021 Simone Caronni <negativo17@gmail.com> - 0-2.20210310gitc539073
- Update postuninstall scriptlet with correct ports.

* Wed Mar 10 2021 Simone Caronni <negativo17@gmail.com> - 0.1-1.20210310git5eccc2a
- First build.

