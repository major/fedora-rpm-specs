Summary: The basic required files for the root user's directory
Name: rootfiles
Version: 8.1
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

BuildArch: noarch

%description
The rootfiles package contains basic required files that are placed
in the root user's account.  These files are basically the same
as those in /etc/skel, which are placed in regular
users' home directories.

%prep

%install
mkdir -p $RPM_BUILD_ROOT/root

for file in %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} ; do
  f=`basename $file`
  install -p -m 644 $file $RPM_BUILD_ROOT/root/${f/dot-/.}
done

%posttrans
if [ $1 -eq 0 ] ; then
  #copy recursively the content, but do not overwrite the original files provided by rootfiles package
  cp -ndr --preserve=ownership,timestamps /etc/skel/. /root/ || :
fi

%files
%config(noreplace) /root/.[A-Za-z]*

%changelog
%autochangelog
