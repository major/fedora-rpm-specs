Summary: The basic required files for the root user's directory
Name: rootfiles
Version: 9.0
Release: %autorelease
License: LicenseRef-Not-Copyrightable

# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Source0: dot-bashrc
Source1: dot-bash_profile
Source2: dot-bash_logout
Source3: dot-tcshrc
Source4: dot-cshrc
Source5: rootfiles.conf

%define ROOTFILES_DIR %{_datadir}/rootfiles

BuildArch: noarch
BuildRequires: systemd-rpm-macros

%description
The rootfiles package contains basic required files that are placed
in the root user's account.  These files are basically the same
as those in /etc/skel, which are placed in regular
users' home directories.

%prep

%install
mkdir -p $RPM_BUILD_ROOT/%{ROOTFILES_DIR}
install -D -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_tmpfilesdir}/rootfiles.conf

for file in %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} ; do
  f=`basename $file`
  install -p -m 644 $file $RPM_BUILD_ROOT/%{ROOTFILES_DIR}/${f/dot-/.}
done

%posttrans
#if [ $1 -eq 0 ] ; then
  #copy recursively the content, but do not overwrite the original files provided by rootfiles package
  # NOTE: This has been broken by the conversion to tmpfiles. I see only one way to make it
  # work: to synthetize a tmpfiles entry for each of these additional files/dirs. That seems like
  # a lot of effort to continue supporting a feature for which there's likely not a high demand...
  # cp -ndr --preserve=ownership,timestamps /etc/skel/. %{ROOTFILES_DIR}/ || :
#fi

%files
%dir %{ROOTFILES_DIR}
%{ROOTFILES_DIR}/.[A-Za-z]*
%{_tmpfilesdir}/rootfiles.conf
%ghost %verify(not md5 size mtime) %attr(0644,root,root) /root/.bash_logout
%ghost %verify(not md5 size mtime) %attr(0644,root,root) /root/.bash_profile
%ghost %verify(not md5 size mtime) %attr(0644,root,root) /root/.bashrc
%ghost %verify(not md5 size mtime) %attr(0644,root,root) /root/.cshrc
%ghost %verify(not md5 size mtime) %attr(0644,root,root) /root/.tcshrc

%changelog
%autochangelog
