Name:           dc3dd
Version:        7.3.1
Release:        %autorelease
Summary:        Patched version of GNU dd for use in computer forensics

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://sourceforge.net/projects/dc3dd/
Source0:        http://downloads.sourceforge.net/dc3dd/%{name}-%{version}.zip

#Fixing build error: automatic de-ANSI-fication support has been removed
#Removing the check for AM_C_PROTOTYPES
Patch1:         dc3dd-01_automake.patch
Patch2:         dc3dd-configure-c99.patch

# Original Archlinux patch to fix build with recent libtools version
# Author: mschlenker
# included upstream in version 7.3.0
# Patch2:         dc3dd-02_fix-FTBFS-with-glibc-2.28.patch


BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gnulib-devel
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  p7zip
BuildRequires:  m4, readline-devel, autoconf, automake
BuildRequires:  make

%description
dc3dd is a patched version of GNU dd to include a number of features useful
for computer forensics. Many of these features were inspired by dcfldd, but
were rewritten for dc3dd.

* Pattern writes. The program can write a single hexadecimal value or a
    text string to the output device for wiping purposes.
* Piecewise and overall hashing with multiple algorithms and variable 
    size windows. Supports MD5, SHA-1, SHA-256, and SHA-512. Hashes can be 
    computed before or after conversions are made.
* Progress meter with automatic input/output file size probing
* Combined log for hashes and errors
* Error grouping. Produces one error message for identical sequential 
    errors
* Verify mode. Able to repeat any transformations done to the input 
    file and compare it to an output.
* Ability to split the output into chunks with numerical or alphabetic 
    extensions


%prep
%autosetup -S git

#Missing x flag in version 7.2.646 makes the build fail
chmod +x build-aux/git-version-gen configure

# ChangeLog having wrong ends of lines
sed -i -e 's|\r||g' ChangeLog


%build
autoreconf -vif #BZ925238 - support aarch64
# TODO check the --enable-hdparm option
%configure 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog README README.coreutils THANKS THANKS-to-translators TODO Sample_Commands.txt NEWS Options_Reference.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
%autochangelog
