# Package is arch'ed because of %%{_libdir}, but we do not build any
# binaries, thus there is no useful debuginfo generated.
# Disabling generation of debuginfo.
%global			debug_package	%{nil}

# Setup location of rpm-macros.
%{!?_macrosdir:%global	_macrosdir	%(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)}

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global	_pkgdocdir	%{_docdir}/%{name}-%{version}}

# Are licenses packaged using %%license?
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%bcond_without		license_dir
%else  # 0%%{?fedora} >= 21 || 0%%{?rhel} >= 8
%bcond_with		license_dir
%endif # 0%%{?fedora} >= 21 || 0%%{?rhel} >= 8

%global			common_description				\
This package holds the common filesystem-layout used by YaST2		\
and handles log-rotation for YaST2-logfiles.


Name:		yast2-filesystem
Version:	0.1.0
Release:	21%{?dist}
Summary:	YaST filesystem layout

License:	Unlicense
URL:		https://en.opensuse.org/Portal:YaST

# Package has no real upstream.  Spec-file was written by me,
# Björn Esser <besser82@fedoraproject.org>, and licensed as
# 'Public Domain', thus I include a matching LICENSE.txt as
# Source0 into the package.
Source0:	http://unlicense.org/UNLICENSE#/LICENSE.txt

BuildRequires:	pkgconfig(yast2-devtools)

%description
%{?common_description}


%prep
%setup -cqT

# Copy-in LICENSE-file.
%{__install} -pm 0644 %{SOURCE0} .

# Create README.txt.
echo "%{?common_description}" | %{__sed} -e '/^$/d' > README.txt


%build
# Create manifest-files.
%{__grep} -e '^%%yast_.*dir ' %{?_macrosdir}/macros.yast |		\
	%{__sed} -e '/%%yast_docdir/d' -e 's!^.*[ \t]\+!!g' |		\
	%{_bindir}/sort -u > mf.list
%{__sed} -e '/^.var.*fillup-templates$/d' -e '/^$/d' -e 's!^!%%dir !g'	\
	< mf.list | %{_bindir}/sort -u > mf.files


%install
# Create dirs from manifest.
for _dir in $(%{__cat} mf.list)
do
	_dir="$(%{_bindir}/rpm --eval ${_dir})"
	%{__mkdir} -p "%{buildroot}${_dir}"
done

# Create config for log-rotate.
%{__mkdir} -p %{buildroot}%{_sysconfdir}/logrotate.d
%{__cat} >> %{buildroot}%{_sysconfdir}/logrotate.d/%{name} << EOF
%{_localstatedir}/log/YaST2/* {
	missingok
	notifempty
	compress
	delaycompress
}
EOF


%files -f mf.files
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/logrotate.d
%doc README.txt
%if %{with license_dir}
%license LICENSE.txt
%else  # %%{with license_dir}
%doc LICENSE.txt
%endif # %%{with license_dir}
%if "%{_libdir}" == "%{_prefix}/lib64"
%dir %{_libdir}/YaST2
%endif # "%%{_libdir}" == "%%{_prefix}/lib64"


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Björn Esser <bjoern.esser@gmail.com> - 0.1.0-1
- initial rpm release (#1218788)

* Mon May 04 2015 Björn Esser <bjoern.esser@gmail.com> - 0.1.0-0.1
- bootstrapping
