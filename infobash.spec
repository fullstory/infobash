#
# spec file for package infobash
#
# Copyright (c) 2005 Stefan Lippers-Hollmann <s.l-h@gmx.de>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://rebelhomicide.demon.nl/scripts/
#

# norootforbuild
# neededforbuild

BuildRequires: cpio diffutils file gzip make man mktemp patch tar

Name:         infobash
URL:          http://rebelhomicide.demon.nl/scripts/
License:      GPL
Group:        System/Packages
Provides:     infobash
Requires:     bash, coreutils, net-tools, procps, pciutils, grep, gawk
Autoreqprov:  on
Version:      2.53
Release:      1
Summary:      System info script for irc
Source:       infobash_%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch

%description
Infobash is a system information script for IRC (Internet Relay Chat) clients.
A system information script can display all kinds of things about your
hardware and software to users in a chatroom,  so they can help you diagnose
problems, ... or just marvel at your system specs and kernel version ;)
It was created to serve the need for a infoscript that isn't dependant on a
particular irc client. Because most irc clients support the /exec command, a
script that runs with /exec would be most portable.



Authors:
--------
    M.L. de Boer <infobash@rebelhomicide.demon.nl>

%prep
%setup
#gzip -d -c infobash_%{version}.tar.gz | tar xf -

%build

%install
# Prepare build root
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT

##
# infobash stuff
##
# prepare directory structure, copy files

install -d -m 0755 $RPM_BUILD_ROOT/etc
install -d -m 0755 $RPM_BUILD_ROOT/usr
install -d -m 0755 $RPM_BUILD_ROOT/usr/bin
install -d -m 0755 $RPM_BUILD_ROOT/opt
install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3
install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3/share
install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3/share/apps
install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3/share/apps/konversation
install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3/share/apps/konversation/scripts

#copy files
install -m 0755 infobash $RPM_BUILD_ROOT/usr/bin/infobash
install -m 0644 infobash.conf $RPM_BUILD_ROOT/etc/
cd $RPM_BUILD_ROOT/opt/kde3/share/apps/konversation/scripts && ln -fs /usr/bin/infobash

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/etc/*
/usr/bin/*
/opt/kde3/share/apps/konversation/scripts/*

%changelog -n infobash
* Thu Jul 18 2005 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - 2.01
* Thu Jul 17 2005 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - 2.00b21
* Thu Jul 14 2005 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - 2.00b20
* Tue Mar 08 2005 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- updated to current version - version 2.00b15
* Sun Oct 10 2004 - Stefan Lippers Hollmann <s.l-h@gmx.de>
- package created - version 2.00b11
