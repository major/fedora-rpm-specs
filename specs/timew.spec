Name:       timew
Version:    1.8.0
Release:    %autorelease
Summary:    Timewarrior tracks and reports time
# SPDX
License:    MIT
URL:        https://timewarrior.net/
# Do not use github tag archives
# They do not contain the libshared git submodule
Source0:    https://github.com/GothenburgBitFactory/timewarrior/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    README.Fedora
# updated bash completion from https://raw.githubusercontent.com/lauft/timew-bashcompletion/refs/heads/master/timew
Source2:    timew-bash-completion

BuildRequires:  cmake gcc-c++
BuildRequires:  rubygem-asciidoctor

%description
Timewarrior is a time tracking utility that offers simple stopwatch features as
well as sophisticated calendar-base backfill, along with flexible reporting. It
is a portable, well supported and very active, Open Source project.

Please read the /usr/share/doc/timew/README.Fedora file on using the included
extensions.

%prep
%autosetup
cp -v %{SOURCE1} .
cp -v %{SOURCE2} completion/timew-completion.bash
chmod -x doc/holidays/*
for lib in doc/holidays/*; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

for lib in ext/*; do
 sed "s@^#!/usr/bin/env python3@#!%{python3}@" $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# Install themes in _datadir instead of _docdir
sed -i 's|DESTINATION.*|DESTINATION ${SHARE_INSTALL_PREFIX}/timew/themes/)|' doc/themes/CMakeLists.txt

%build
%cmake -DTIMEW_BINDIR=%{_bindir} -DTIMEW_DOCDIR=%{_pkgdocdir} -DTIMEW_MAN1DIR=%{_mandir}/man1/ -DTIMEW_MAN7DIR=%{_mandir}/man7/
%cmake_build

%install
%cmake_install

# move extensions to datadir and keep shebang
install -m 0755 -d $RPM_BUILD_ROOT/%{_libdir}/%{name}/
mv $RPM_BUILD_ROOT/%{_pkgdocdir}/ext $RPM_BUILD_ROOT/%{_libdir}/%{name}/ -v
chmod +x $RPM_BUILD_ROOT/%{_libdir}/%{name}/ext/*

# Not needed
rm -f $RPM_BUILD_ROOT/%{_docdir}/%{name}/INSTALL
# same as license
rm -f $RPM_BUILD_ROOT/%{_docdir}/%{name}/LICENSE

# Install Fedora readme file
mv -v README.Fedora $RPM_BUILD_ROOT/%{_pkgdocdir}/

# Install bash completion file
install -m 0755 completion/timew-completion.bash -DT $RPM_BUILD_ROOT/%{bash_completions_dir}/timew
install -m 0755 completion/timew.fish -DT $RPM_BUILD_ROOT/%{fish_completions_dir}/timew.fish

%check
# Run tests
make test %{_smp_mflags}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man7/%{name}*
%{_pkgdocdir}/
%{bash_completions_dir}
%{fish_completions_dir}

%changelog
%autochangelog
