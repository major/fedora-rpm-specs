# Partially generated by rust2rpm 27
%bcond check 1

# prevent library files from being installed
%global cargo_install_lib 0

# Temporarily use a Git revision until next stable release
%global commit           e16b4abffc5e23d20e49de5f1461aebfc692268d
%global shortcommit      %{sub %{commit} 1 7}
%global commitdate       20250710

# icu soversion
%global icu_sover 76
%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif

Name:           msedit
Version:        1.2.0^1.%{shortcommit}
Release:        %autorelease
Summary:        Simple editor inspired by the MS-DOS Editor
SourceLicense:  MIT
# MIT OR Apache-2.0: libc v0.2.172
# MIT: edit v1.2.0
License:        MIT AND (MIT OR Apache-2.0)

URL:            https://github.com/microsoft/edit
Source:         %{url}/archive/%{shortcommit}.tar.gz
Patch:          edit-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  desktop-file-utils
BuildRequires:  libicu-devel

# For dlopen() libicu
Requires:       libicuuc.so.%{icu_sover}%{?lib64_suffix}
Requires:       libicui18n.so.%{icu_sover}%{?lib64_suffix}

%global _description %{expand:
%{summary}

A text editor that pays homage to the classic MS-DOS Editor, but with a modern
interface and input controls similar to VS Code. The goal is to provide an
accessible editor that even users largely unfamiliar with terminals can easily
use.
}

%description %{_description}

%prep
%autosetup -n edit-%{commit} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# Set environment variables for ICU libraries
EDIT_CFG_ICUUC_SONAME=libicuuc.so.%{icu_sover}
EDIT_CFG_ICUI18N_SONAME=libicui18n.so.%{icu_sover}

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

# de-conflict with vim
mv %{buildroot}%{_bindir}/edit %{buildroot}%{_bindir}/%{name}

# Change binary and icon in .desktop file then install it
sed -i \
    -e "s|Icon=edit|Icon=%{_datadir}/pixmaps/%{name}.ico|g" \
    -e "s|Exec=edit %%F|Exec=%{name} %%F|g" assets/com.microsoft.edit.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications assets/com.microsoft.edit.desktop

# Install icon
install -Dpm 0644 assets/edit.ico %{buildroot}%{_datadir}/pixmaps/%{name}.ico
install -Dpm 0644 assets/edit.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Change manpage to match binary name and install it
sed -i \
    -e "s|edit |msedit |g" \
    -e "s|EDIT 1|MSEDIT 1|g" \
    -e "s|fBedit|fBmsedit|g" assets/manpage/edit.1
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 assets/manpage/*.1
mv %{buildroot}%{_mandir}/man1/edit.1 %{buildroot}%{_mandir}/man1/%{name}.1

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%{_bindir}/%{name}
%{_datadir}/applications/com.microsoft.edit.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.ico
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
