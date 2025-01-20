Summary: RPM local_generator support
Name: rpm-local-generator-support
Version: 1
Release: 7%{?dist}

# It is not really clear if the one empty file shipped by this package is even
# copyrightable. But let's go with GPLv2+ which is the license used by RPM,
# where this file should ideally come from or be replaced by different
# implementation.
#
# The license was discussed in this thread:
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/X6RUQK5R6KIMVIQ6FQPNVGTJJXSNRD4V/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://src.fedoraproject.org/rpms/rpm-local-generator-support
Source1: README.md
BuildArch: noarch

%description
local_generator.attr file enabling RPM dependency generator to be used on .spec
files, which ships them.



%prep


%build


%install
cp %{SOURCE1} .

install -d %{buildroot}%{_fileattrsdir}
touch %{buildroot}%{_fileattrsdir}/local_generator.attr


%files
%doc README.md
%{_fileattrsdir}/local_generator.attr



%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 13 2024 Dridi Boukelmoune <dridi@fedoraproject.org> - 1-6
- Tweak RPM spec for compatibility with EPEL 8

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1-5
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 06 2023 Vít Ondruch <vondruch@redhat.com> - 1-1
- Initial version.
